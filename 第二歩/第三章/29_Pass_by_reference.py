# 変数aを用意
a = ["apple", "orange", "banana"]

# 変数a_idに変数aの識別番号を代入
a_id = id(a)

# 変数aの識別番号を出力
print(a_id)

# 変数seeにaを参照渡し
see = a

# 変数seeを出力、変数aの中身が参照可能なことを確認
# print(see)

# 変数see_idに変数seeの識別番号を代入
see_id = id(see)

# 変数seeの識別番号を出力
print(see_id)

# 変数aと変数seeの識別番号が一致しているかを確認
print(a_id == see_id)

# 変数seeの中身を更新
see[0] = "ピーマン"

# 変数aの中身を出力、変数aの中身も書き換わってしまっていることを確認
print(a)