# ローカル変数だと関数の外での更新はできない
def hello():
    local = "Hello"
    print(local)

# 変数の更新
local = "apple"

# 関数の実行
hello()