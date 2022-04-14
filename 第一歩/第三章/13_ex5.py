# 以下のプログラムを実行し｢yes｣と入力したとき｢どのような返り｣が表示されるでしょうか。
# 正しいと思う解答を１つ選んでください。

iterable = range(100)
for i in iterable:
    #print(i)
    if i == 10:
        break
if i < 20:
    print("Thank you")