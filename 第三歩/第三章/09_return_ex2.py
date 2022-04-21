# それでは,以下のプログラムを完成させて｢関数の実行結果｣を｢変数に保存｣し,
# 次に｢標準出力｣により,変数の内容をShellに表示してください。
# 以下の関数は｢あなたのお名前｣を｢引数｣として｢関数に入力｣すると｢◯◯さん Hello!｣と返すhello()関数です。

def hello(arg=None):
    return f"{arg}さん Hello!"

y = hello("nagapon")
print(y)