# fromで定数piのみを指定してimportしているため、math.pyは使用できない

from math import pi

y = math.fabs(-100)
print(y)