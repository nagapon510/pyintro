# グローバル変数を関数の中で変更しようとするとエラーになる
GLOBAL = "Hello"

def hello(arg=None):
    GLOBAL += " World"
    print(GLOBAL)

hello()