# 以下の｢リスト型のデータ構造を持つ変数basket｣において｢変数x｣に｢値渡し｣をしてください。
# その次に｢値渡し｣の確認のために,それぞれの｢id：識別番号｣も確認してください。

basket = ["apple", "orange", "banana"]
x = basket[:]
print(id(basket))
print(id(x))
print(id(basket) == id(x))