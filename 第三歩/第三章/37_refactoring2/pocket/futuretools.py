# futuretools.py

import rangefunction as rf

# 関数の定義
def doublebox(arg=None):
    if arg is None:
        arg = input("Please, arg \n>>> ")

    if arg != None:
        for i in rf.rangef2(2):
            print(arg)

# 関数の定義
def triplebox(arg=None):
    if arg is None:
        arg = input("Please, arg \n>>> ")

    if arg != None:
        for i in rf.rangef2(3):
            print(arg)