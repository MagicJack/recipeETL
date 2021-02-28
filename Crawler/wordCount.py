import os, sys, json

from clnIngred import ingCleaner

folders = ["低脂","生酮","低醣","沙拉","高蛋白","健身","高纖"]

cntTotal = 0
cntProcs = 0
foodList = []
foodFreq = {}

nClean = int(sys.argv[1])  if len(sys.argv) > 1 else 4
bVerb  = bool(sys.argv[2]) if len(sys.argv) > 2 else False

def load_ID(path):
    ID_file = path
    ID_dict = set()
    # if not os.path.isfile(ID_file):
    #     return ID_dict
    try:
        with open(ID_file, "r", encoding='utf-8') as f:
            for line in f:
                ID_dict.add(line.replace('\n', ''))
    except:
        print('No excluding list loaded.')
    return ID_dict

ng_ID = load_ID('ID_exclude.txt')
skip_ID = set()

cleaner = ingCleaner()

def procIngrdent(food_ID, ingreds):
    global foodList, foodFreq, cntTotal
    global cleaner

    for food, qty in ingreds.items():  # 抓出"食譜"中的所有 key 和 值
        if nClean:
            nfood = cleaner.cleanIng(food_ID, food, bVerb=bVerb, nClean=nClean)
        else:
            nfood = food

        if cleaner.checkSkip(food_ID, nfood, qty, bVerb=True) > 0:
            skip_ID.add(food_ID)
            # continue

        # 計算食材出現詞頻
        if nfood in foodList:
            foodFreq[nfood] += 1
        else:
            foodFreq[nfood] = 1
        foodList.append(nfood)
        #print(food) # 所有食材

for i in folders:
    with open(f'{i}/{i}.txt', 'r', encoding='utf-8') as f:
        for line in f:              # 使用迴圈方式一條一條抓
            data = json.loads(line)
            cntTotal += 1
            food_ID = data['food_ID']
            if food_ID not in ng_ID:
                procIngrdent(food_ID, data['食譜'])
                cntProcs += 1

skipA, skipB, skipC = cleaner.getSkip()
print(f"少許:{len(skipA)}\nList:{skipA}\n\n適量:{len(skipB)}\nList:{skipB}\n\n空白:{len(skipC)}\nList:{skipC}\n")
print(f'To Skip:{len(skip_ID)}\nList:{skip_ID}')

print(len(foodList)) # 總共多少食材
print(cntTotal, cntProcs) # 總共幾個食譜


# 詞頻轉成表格
import pandas as pd
df = pd.DataFrame.from_dict(foodFreq, orient='index', columns=['詞頻']) # 將字典轉為表格

# df = df.sort_index(ascending=False)
# df.to_csv("照食材順序排的food_frequency_2.0.csv", encoding="utf-8-sig")

df = df.sort_values(by='詞頻', ascending=False) # 照"詞頻"這欄的值，由大到小做排列 ascending=False
df.to_csv("照詞頻順序排的food_frequency_2.0.csv", encoding="utf-8-sig")
