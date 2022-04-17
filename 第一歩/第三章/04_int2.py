x = input("魚は何グラム？ \n>>> ")
x = int(x)

if x < 500:
    print("川に戻しました")
else:
    print("バケツに入れました")