# 以下のプログラムを実行すると｢どのような返りになるか｣正しいと思う解答を1つ選んでください。

x = 1 + (2 + 3) * 4
if type(float(x)) != type(int(x)):
    print("float is not integer")