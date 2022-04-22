# 関数の定義
def rangef2(start=0, stop=None, step=1):
    while start < stop:
        yield start
        start += step

# 関数の呼び出し
for i in rangef2(1, 10, 2):
    print(f"{i} ", end="")