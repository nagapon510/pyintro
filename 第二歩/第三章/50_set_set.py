# range関数の場合 -> 数値においては昇順で返す
print("-" * 50)
print("range()関数の場合")

rng = range(5)
print(rng)
print(set(rng))

# 文字列の場合 -> indexを持たないため順序はhash、重複を削除
print("-" * 50)
print("文字列の場合")

str = "apple"
print(str)
print(set(str))

# タプルの場合 -> indexを持たないため順序はhash
print("-" * 50)
print("タプルの場合")

tpl = ("apple", "orange", "banana")
print(tpl)
print(set(tpl))

# リストの場合 -> indexを持たないため順序はhash
print("-" * 50)
print("リストの場合")

lst = ["apple", "orange", "banana"]
print(lst)
print(set(lst))

# ディクショナリの場合 -> indexを持たないため順序はhash、keyのみが返却
print("-" * 50)
print("ディクショナリの場合")

dic = dict(apl="apple", org="orange", bnn="banana")
print(dic)
print(set(dic))

# エラーパターン -> イテラブルでないものをsetするとエラー
print("-" * 50)
print("エラーパターン")

err = 1
print(err)
print(set(err))