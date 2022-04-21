# 関数の中で定義された変数は関数の外では使用できない
def hello():
    local = "Hello"

#print(local) #外で使用


# 関数の中では使用可能
def hello():
    local = "Hello"
    print(local) #中で使用

hello()