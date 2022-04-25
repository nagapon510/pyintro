# playgame.py
import random as rd

# 関数の定義
def chohan():
    # 標準入力
    ans = input("cho or han !? \n>>> ")

    # サイコロをふる:method
    sai = rd.randint(1, 6)

    # 偶数の場合
    if sai % 2 == 0 and ans == "cho":
        print(f"{sai} is cho ! You Win !")

    # 奇数の場合
    if sai % 2 == 1 and ans == "han":
        print(f"{sai} is han! You Win !")
    else:
        print("You Lose...")

# 関数の呼び出し
if __name__ == "__main__":
    chohan()