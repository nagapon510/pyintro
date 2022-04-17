# 以下のプログラムを実行すると,どのような返りがあるでしょうか。1つ解答を選択してください。

time = ("朝飯は", "昼飯は", "夜飯は")
meal = ("apple", "orange", "banana")

for t, m in zip(time, meal):
    print(t, m, "です。")