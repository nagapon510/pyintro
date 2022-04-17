# 変数basketを用意
basket = ["apple", "orange", "banana"]

# 変数basket_idに変数basketの識別番号を代入
basket_id = id(basket)

# 変数basketの識別番号を出力
print(basket_id)

# 変数xに値渡し
x = basket[:]

# 変数x_idに変数xの識別番号を代入
x_id = id(x)

# 変数xの識別番号を出力
print(x_id)

# 変数basketと変数xの識別番号が異なることを確認
print(basket_id == x_id)

# 変数xの中身を更新
x[0] = "ピーマン"

# 変数basketの中身を出力、変数basketの中身は書き換わっていないことを確認
print(basket)

# 念のため変数xの中身を確認
print(x)