# 以下のプログラムを実行すると,どのような返りがあるでしょうか。1つ解答を選択してください。

basket = ["apple", "orange", "banana"]
see = basket
#print(id(basket), id(see))

result = len(basket) < len(see)
#print(result)

if result:
    dic_f = dict(fruit="apple")
    print(dic_f)
else:
    dic_f = dict(fruit="orange")
    print(dic_f)