# 以下のrangef2()関数の定義において｢同等性確認｣よりも｢同一性確認｣にした方が良いと思うところを,
# リファクタリングしてください。

# rangef2.py

# 関数の定義
def rangef2(start=0, stop=None, step=1):
    if stop is None:
        start, stop = 0, start

    while start < stop:
        yield start
        start += step

# 関数の呼び出し
for i in rangef2(10):
    print(f"{i} ", end="")