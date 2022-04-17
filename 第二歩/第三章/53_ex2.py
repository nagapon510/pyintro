# 以下のプログラムを実行すると,どのような返りがあるでしょうか。1つ解答を選択してください。

'''奇数の数を求めるプログラムです'''

number = (0, 1, 2, 3, 4, 5, 6, 7, 8)
odd_num = list()

for num in number:
    if num % 2 == 1:
        odd_num += [num]
        #print(f"{num} は奇数です。")
    
result = len(odd_num)
print(f"奇数の数は {result}つ　です。")