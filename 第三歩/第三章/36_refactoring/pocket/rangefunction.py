# rangefunction.py

# 関数の定義
def rangef2(start=0, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    
    while start < stop:
        yield start
        start += step