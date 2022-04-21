def pay():
    time = int(input("usage time !? \n>>> "))
    variable = 10 * time
    fixed = 5000
    payment = variable + fixed
    print(f"今月のスマホ代は{payment}円です。")

def payfor():
    for i in range(4):
        pay()

payfor()