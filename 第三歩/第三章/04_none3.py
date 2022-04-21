# 引数を指定していない場合入力を要求する仕様に変更
def doublebox(arg=None):
    if arg == None:
        arg = input("Please, arg! \n>>> ")
    
    if arg != None:
        for i in range(2):
            print(arg)

# 引数指定なしで実行
doublebox()