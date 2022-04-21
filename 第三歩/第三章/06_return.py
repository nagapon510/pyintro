# 標準出力を使用
def doublebox_stdout(arg=None):
    print(arg)

# 関数の呼び出し
doublebox_stdout()


# returnを使用
def doublebox_return(arg=None):
    return(arg)

# 関数の呼び出し ⇒ 出力
y = doublebox_return()
print(y)