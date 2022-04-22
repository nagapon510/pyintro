# 反復回数を入力式に
def loop(time=0):
    num = int(input("number !? \n>>> "))
    while time < num:
        print("Hello World")
        time += 1

loop()