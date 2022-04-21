print(type(None))

# デフォルト引数をNoneで定義
def doublebox(arg=None):
    for i in range(2):
        print(arg)

doublebox()