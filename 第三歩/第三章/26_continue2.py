# 関数化
def oddloop(time=0):
    num = int(input("number !? \n>>> "))
    while time < num:
        time += 1
        if time % 2 == 0:
            continue
        print(time)

oddloop()