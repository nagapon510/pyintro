# 標準出力パターン
GLOBAL = "Hello"

def hello(arg=None):
    print(GLOBAL)

hello()

# returnパターン
GLOBAL = "Hello"

def hello(arg=None):
    return GLOBAL

y = hello()
print(y)