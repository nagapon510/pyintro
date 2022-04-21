# global文を使用
GLOBAL = "Hello"

def hello(arg=None):
    global GLOBAL

    GLOBAL += " World"
    print(GLOBAL)

hello()