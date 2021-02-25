import requests
import os
import json
import sys
import traceback
import urllib
import random
import emoji
import re
from bs4 import BeautifulSoup
from time import sleep


def save_total_json(keyword):
    fp = keyword
    file_folder = f'./{fp}/'
    with open(file_folder + f'{fp}'+ ".txt", 'r', encoding='utf-8') as load_f:
        load_list = load_f.read().split('\n') #把每筆資料整理成 list列表
        load_list.remove("")

    for i, j in enumerate(load_list):
        load_list[i] = json.loads(j)

    with open(file_folder + f'{fp}'+ ".json", 'w', encoding='utf-8') as load_f:
        json.dump(load_list, load_f, ensure_ascii=False)
    print("finished")

def load_ID(path):
    ID_file = path
    ID_dict = {}
    if os.path.isfile(ID_file):
        with open(ID_file, "r", encoding='utf-8') as f:
            for line in f.readlines():
                if line != "":
                    ID_dict[line.split('\n')[0]] = True
    else:
        with open(ID_file, "w", encoding='utf-8') as f:
            f.write("")
    return ID_dict

def clean_emotion(data_str):
    data = str(data_str)
    text = emoji.demojize(data)
    ret = re.sub(':\S+?:', ' ', text)
    result = ret
    return result

def clean_data(data_str, type_name):
    data = data_str
    if type_name == "食材名稱":
        # data_recipe = clean_emotion(data)
        # a = data_recipe.split(' ')[0]
        # b = a.split('(')[0]
        # c = b.split('（')[0]
        # d = c.split('[')[0]
        # e = d.split('［')[0]
        # result1 = e.split('〈')[0]
        # return result1
        return clean_emotion(data)

    elif type_name == "食材份量":
        # data_recipe = clean_emotion(data)
        # g1 = data.replace("公克", "g")
        # g2 = g1.replace("克", "g")
        # # 這邊可以繼續接著處理各種 case
        # result2 = g2
        # return result2
        return clean_emotion(data)

    elif type_name == "步驟":
        # data_step = clean_emotion(data)
        # result3 = data_step
        # return result3
        return clean_emotion(data)

    else:
        print("Wrong type_name")
        return data

def recipes(food):
    keyword = food
    try:
        os.makedirs(keyword) #為該 keyword 創建一個資料夾
    except FileExistsError:
        pass

    foodWordUrl = urllib.parse.quote(keyword)
    userAgent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    page = 1
    count = 0
    food_Info = {}
    ID_dict = load_ID("ID_list.txt")
    #print(ID_dict)
    while page <= 1000:
        url = 'https://icook.tw/search/' + foodWordUrl + '/?page=' + str(page)
        print(url)
        headers = {'User-Agent': userAgent, 
                   'Referer': url}
        req = requests.get(url, headers = headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        recipes = soup.select('li.browse-recipe-item')
        check_page = soup.select('h1')[0]

        if check_page.text.strip()[:11] == "唉啊! 這個頁面不見了":
            page-=1
            print(f"{food}最多搜尋至{page}頁")
            print("==================================="*3)
            break
        elif check_page.text.strip()[:11]=="網站正在維護升級中，請":
            page+=1
            if count <= 20:
                count+=1
                print("網頁維戶升級中")
                print("==================================="*3)
                continue
            else:
                page-=(count+2)
                print(f"{food}最多搜尋至{page}頁")
                print("==================================="*3)
                break
        #print(f'ID list : {ID_dict}')

        for href in recipes:
            aTag = href.select_one('a')['href']
            ID = aTag.split('/')[2]

            if ID in ID_dict:
                print("ID already existed")
                continue
            else:
                with open("ID_list.txt", "a", encoding='utf-8') as f:
                    f.write(ID)
                    f.write("\n")
                food_Info["food_ID"] = ID # 插入 ID
                ID_dict[ID]= True
                recipeName = href.select_one('h2.browse-recipe-name')['data-title']
                recipeName_ret = clean_emotion(recipeName)
                food_Info["菜名"] = recipeName_ret # 插入菜名
                recipesUrl = 'https://icook.tw' + str(aTag)
                food_Info["url"] = recipesUrl # 插入 url

                recipesHeaders = {'User-Agent': userAgent, 'Referer': recipesUrl}
                recipesReq = requests.get(recipesUrl, headers = recipesHeaders)
                recipesSoup = BeautifulSoup(recipesReq.text, 'html.parser')

                ranking = recipesSoup.select('span.stat-content')[0].text #推讚數
                try:
                    food_Info["推讚數"] = ranking.split(' ')[0]
                except Exception as e:
                    #print(f'推讚數 error: {e}')
                    food_Info["推讚數"] = None


                try:
                    viewing = recipesSoup.select('div.recipe-detail-meta-item')[0].text #瀏覽數
                    food_Info["瀏覽數"] = viewing.strip().split(' ')[0]

                except Exception as e:
                    #print(f'瀏覽數 error: {e}')
                    food_Info['瀏覽數'] = None

                try:
                    description = recipesSoup.select('div.description')[0].text #料理簡介
                    if description.split()[0] =='null':
                        food_Info["料理簡介"] = None
                    else:
                        food_Info["料理簡介"] = clean_emotion(description.split()[0])
                except Exception as e:
                    #print(f'料理簡介 error: {e}')
                    food_Info["料理簡介"] = None

                try:
                    servingNum = recipesSoup.select('span.num')[0].text #份數的數字
                    #servingUnit = recipesSoup.select('span.unit')[0].text #份數的單位
                    food_Info["份數"] = f'{servingNum}'
                except Exception as e:
                    #print(f'份數 error: {e}')
                    food_Info["份數"] = None

                food_Info["食譜"]={}
                #food_Info["食譜"]=[]
                food_Info["步驟"]=[]
                recipePage = recipesSoup.select('div.row')

                ingre = recipePage[3]
                for n in range(len(ingre.select('a.ingredient-search'))):
                    #food_dict ={}
                    ingre1 = ingre.select('a.ingredient-search')[n].text #食材的名稱
                    ingre_ret = clean_data(ingre1, "食材名稱")
                    unit1 = ingre.select('div.ingredient-unit')[n].text #食材的分量
                    unit_ret = clean_data(unit1, "食材份量")
                    #food_dict[ingre1] = unit1
                    #food_Info["食譜"].append(food_dict)
                    food_Info["食譜"][ingre_ret]= unit_ret

                for m in range(len(ingre.select('p.recipe-step-description-content'))):
                    #step_dict = {}
                    step = ingre.select('p.recipe-step-description-content')[m].text #食材的步驟
                    step_ret = clean_data(step, "步驟")
                    #step_dict[f"step{m+1}"]= step_ret
                    #food_Info["步驟"].append(step_dict)
                    food_Info["步驟"].append(step_ret)
                    file = f'./{keyword}/{keyword}.txt'
                with open(file, "a", encoding='utf-8') as f: #存成 json格式
                    json.dump(food_Info, f, ensure_ascii= False)
                    f.write('\n')
                    print("")
                    print(f"ID:{ID}\n已載入入檔案完成...")
                    print("==================================="*3)
                food_Info.clear()

        sleep(random.uniform(1, 3))
        page += 1
    save_total_json(keyword) # 將暫存的每筆到 txt內容，整理成一包大 json 格式檔案


keyword = ["低脂", "生酮", "低醣", "沙拉", "高蛋白", "健身", "高纖"]  # 輸入查詢關鍵字 list


for k in keyword:
    recipes(k)
    print(f"{k}: 已全部完成")
    print("==================================="*3)

for i in keyword:
    with open(f'./{i}/{i}.json', 'r', encoding='utf-8') as correct_reader:
        c_list = json.load(correct_reader) # json.load()內，是要給檔案物件(不能放檔案物件內的string) =>轉成 pyhton看得懂的格式型態
        #c_list = json.loads(reader.read()) # json.loads()內，是要給檔案物件內的 json格式 string
        print(len(c_list))


wrong_json_fp = 'wrong_format.json'
if os.path.exists(wrong_json_fp):
    try:
        with open(wrong_json_fp, 'r', encoding='utf-8') as wrong_reader:
            c_list = json.loads(wrong_reader.read()) #若檔案格式不符合json格式，則會出錯誤訊息
            print(c_list)
    except Exception as e:
        #print(e)
        print("Error message as below:", end ="\n\n")
        error_class = e.__class__.__name__ #取得錯誤類型
        detail = e.args[0] #取得詳細內容
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName = lastCallStack[2] #取得發生的函數名稱
        errMsg = "File: \"{}\"\nline {} in {}: [{}]\n{}".format(fileName, lineNum, funcName
                                                            , error_class, detail)
        print(errMsg) #該格式檔案有換航空格，無法直接讀取
else:
    print('No Error on Json files')
