# 以下のプログラムを実行したとき｢どのような返り｣が表示されるでしょうか。
# 正しいと思う解答を１つ選んでください。

for i in range(100):
    if i > 98:
        print("number is ", i)
print("offset of range() is ", i + 1)