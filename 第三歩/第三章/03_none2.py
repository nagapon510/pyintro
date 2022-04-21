# 引数が指定されていない場合はデフォルト値を一度だけ返す仕様に変更
def doublebox(arg=None):
    if arg == None:
        print(arg)
    else:
        for i in range(2):
            print(arg)

# 引数指定なしで実行
doublebox()

# 引数を指定して実行
doublebox("どらやき")