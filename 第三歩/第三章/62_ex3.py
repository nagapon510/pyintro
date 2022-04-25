# 今日は,海に｢お魚釣りの上級コース｣に来ています。
# そのため｢つけるエサの大きさ｣と,その｢エサを食べる魚｣が,ちゃんと合わないと,釣ることができません。
# たとえば,
# ①たいを釣りたいときはbigなエサ
# ②ひらめを釣りたいときはsmallなエサ
# ③お魚とエサが合わなかったときは,めずらしいものが釣れます・・・
# 以下の｢ソース・コード｣を｢完成｣させて｢お魚釣りの上級コース｣を｢実行：F5｣してください。

# fishing_ver2.py
import random as rd

FISH = {1:"たい", 2:"ひらめ", 3:"にぼし"}

def fishing():
    get = rd.randint(1, 3)
    return FISH[get]

def add_food():
    y = fishing()
    fd = input("big or small !? \n>>> ")

    if y == "たい" and fd == "big":
        print(f"{y}が釣れました♪")
    elif y == "ひらめ" and fd == "small":
        print(f"{y}が釣れました♪")
    else:
        print(f"{FISH[3]}が釣れました...")

if __name__ == "__main__":
    add_food()