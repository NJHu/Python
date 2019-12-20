"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
"""

x = float(input("please input a num"))
y = 0

if x > 1 :
    y = 3 * x - 5
else:
    if x >= -1 and x <= 1 :
        y = x + 2
    else :
        y = 5 * x + 3

print("y is %.0f" % (y))