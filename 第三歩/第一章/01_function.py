# 通話時間を入力する
time = int(input("usage time !? \n>>> "))

# 1分あたりの通話料金10円 × 通話時間
variable = 10 * time

# 基本料金5,000円
fixed = 5000

# 今月のスマホ代
payment = variable + fixed

# Shellに表示する
print(f"今月のスマホ代は{payment}円です。")