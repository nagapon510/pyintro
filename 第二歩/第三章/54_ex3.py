# 今日はBEARが,森に果物をとりにやってきました。
# とてもがんばったので｢カゴ2つ｣がいっぱいになりました。
# いったいBEARは｢何種類の果物｣を得ることができたでしょうか。

'''何種類の果物を得たでしょうか'''

basket_1 = {"apple", "orange", "apple", "apple", }
basket_2 = {"apple", "apple", "apple", "banana", }

fruit = basket_1 | basket_2
#print(fruit)

num = len(fruit)
print(f"BEARは {num}種類 の果物を得ました。")