# 以下の｢リスト型のデータ構造を持つ変数basket｣において｢変数see｣ に｢参照渡し｣をしてください。
# その次に｢参照渡し｣の確認のために,それぞれの ｢id：識別番号｣も確認してください。

basket = ["apple", "orange", "banana"]
see = basket
print(id(basket))
print(id(see))
print(id(basket) == id(see))