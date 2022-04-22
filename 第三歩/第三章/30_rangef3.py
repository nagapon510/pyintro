# rangef2.py

# 関数の定義
def rangef2(start=0, stop=None, step=1):
    if stop == None:
        # 入れ替えアルゴリズム
        start, stop = 0, start
    
    while start < stop:
        # 本文
        yield start

        #停止要件
        start += step

# 関数の呼び出し
for i in rangef2(10):
    print("Hello World", i)