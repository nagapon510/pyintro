# returnが実行された時点で終了することを確認
def doublebox(arg=None):
    if arg == None:
        arg = input("Please, arg \n>>> ")
    
    if arg != None:
        for i in range(100):
            return i

y = doublebox()
print(y)

# for文の使用をやめ、f-stringsでの記載に変更
def doublebox(arg=None):
    if arg == None:
        arg = input("Please, arg \n>>> ")
    
    if arg != None:
        return f"{arg} \n{arg}"

y = doublebox()
print(y)