# rangefunc.py

TIME = 0 #ローカル変数にすると無限ループになる(再帰の都度0にリセットされる)のでグローバル変数にする

# 関数の定義
def rangef(arg=None):
    global TIME

    if TIME == arg:
        return
    else:
        print(TIME)
        TIME += 1

        # 関数の呼び出し：再帰
        rangef(arg)

# 関数の呼び出し
rangef(10)