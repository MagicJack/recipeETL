import sys, json

from clnIngred import ingCleaner

folders = ["低脂","生酮","低醣","沙拉","高蛋白","健身","高纖"]

count = 0
foodList = []
foodFreq = {}

nClean = int(sys.argv[1])  if len(sys.argv) > 1 else 4
bVerb  = bool(sys.argv[2]) if len(sys.argv) > 2 else False

cleaner = ingCleaner()
for i in folders:
    with open(f'{i}/{i}.txt', 'r', encoding='utf-8') as f:
        for line in f:              # 使用迴圈方式一條一條抓
            data = json.loads(line)
            count += 1
            for food, qty in data['食譜'].items():  # 抓出"食譜"中的所有 key 和 值
                if nClean:
                    nfood = cleaner.cleanIng(data['food_ID'], food, bVerb=False, nClean=4)
                    # if food == "鹽巴":
                    #     print('1')
                    if cleaner.checkSkip(data['food_ID'], nfood, qty, bVerb=False):
                        continue
                else:
                    nfood = food

                if nfood in foodList:
                    foodFreq[nfood] += 1
                else:
                    foodFreq[nfood] = 1
                foodList.append(nfood)
                #print(food) # 所有食材
print(len(foodList)) # 總共多少食材
print(count) # 總共幾個食譜
skip = cleaner.getSkip()
print(f"少許: {skip[0]}, 適量:{skip[1]}")


# # 計算食材出現詞頻
# foodFreq = {}
# for i in foodList:
#     if i in foodFreq:
#         foodFreq[i] += 1
#     else:
#         foodFreq[i] = 1
# print(foodFreq)

# 詞頻轉成表格
import pandas as pd
df = pd.DataFrame.from_dict(foodFreq, orient='index', columns=['詞頻']) # 將字典轉為表格

# df = df.sort_index(ascending=False)
# df.to_csv("照食材順序排的food_frequency_2.0.csv", encoding="utf-8-sig")

df = df.sort_values(by='詞頻', ascending=False) # 照"詞頻"這欄的值，由大到小做排列 ascending=False
df.to_csv("照詞頻順序排的food_frequency_2.0.csv", encoding="utf-8-sig")
