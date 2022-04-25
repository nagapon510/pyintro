# 今日は,海に｢お魚釣り｣に来ています。
# 以下の｢ソース・コード｣を実行すると,どのような返りになるでしょうか。
# 正解を1つ選んでください。

# fishing.py

import random as rd

FISH = {1:"たい", 2:"ひらめ", 3:"にぼし"}

def fishing():
    get = rd.randint(1, 3)
    return FISH[get]

y = fishing()
print(f"{y}が釣れました♪")