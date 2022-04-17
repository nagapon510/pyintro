# このプログラムを実行すると｢入力が求められます｣。
# そこで,このプログラムを以下の４人にそれぞれ実行してもらいました。
# ｢お酒を飲むことはできません！：No!Youcan’tdrink!｣と言われてしまうのは｢だれ｣でしょう。
# 正しいと思う解答を１つ選んでください。

age = input("How old are you? \n>>> ")
if int(age) >= 20:
    print("OK! You can drink!")
else:
    print("No! You can't drink!")
