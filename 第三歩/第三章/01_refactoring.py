# 関数の定義
#def doublebox(arg):
#    for i in range(2):
#        print(arg)

# 引数を設定しないとエラーが発生する。
#doublebox()

# デフォルト値を設定
def doublebox(arg="Hello"):
    for i in range(2):
        print(arg)

# 引き数を指定せずに実行するとデフォルト値が返る
doublebox()