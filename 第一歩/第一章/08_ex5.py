#パイソン大学の定期テストがありました。
# そこで,あなたが ｢75 点｣であったとき,平均点より高かったのか,それとも低かったのかを｢プログラム(計算)を書いて｣調べてください。

import numpy as np

MyScore = 75
ScoreList = np.array([75, 85, 65, 40, MyScore])

if np.mean(ScoreList) < MyScore:
    print("high")
else:
    print("low")