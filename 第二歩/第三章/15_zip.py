index = ("0", "1", "2")
value = ("apple", "orange", "banana")

# zip -> umpacking
for i, v in zip(index, value):
    print(i, v)

# umpackingなし
for i in zip(index, value):
    print(i)