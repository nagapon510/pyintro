# IDの出力を追加
def doublebox(arg=None):
    if arg == None:
        print(f"arg ID is {id(arg)}")

        arg = input("Please, arg! \n>>> ")
        print(f"arg ID is {id(arg)}")
    
    if arg != None:
        for i in range(2):
            print(arg)

doublebox()