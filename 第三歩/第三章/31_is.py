# 同一性確認
x = 100
x_id = id(x)
print(f"x is {x_id}")

y = x
y_id = id(y)
print(f"y is {y_id}")

result = x is y
print(result)