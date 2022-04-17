dictionary = {
    "apple":"りんご",
    "orange":"みかん",
    "banana":"バナナ"
}

# 名前が返る
for i in dictionary:
    print(i)

# 要素が返る
for i in dictionary:
    print(dictionary[i])

#いい感じの書き方
for key in dictionary:
    value = dictionary[key]
    print(key, value)