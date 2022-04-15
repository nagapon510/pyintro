# 以下のプログラムを実行すると,どのような返りがあるでしょうか。
# 1つ解答を選択してください。

x = "apple"
y = "orange"

x_type = type(x)
y_type = type(y)

if x_type == y_type:
    print("x and y = string")
else:
    print("x and y = not string")