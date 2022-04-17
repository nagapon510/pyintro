# 以下のプログラムを実際に書いて実行してください。

'''名前と性別と好物を質問するプログラムです'''

fix_question = ("名前", "性別", "好物")
info_dict = {}

for key in fix_question:
    value = input(f"{key}は何ですか？\n>>> ")
    info_dict[key] = value

for key in info_dict:
    value = info_dict[key]
    print(f"\nあなたの{key}は {value} です。")