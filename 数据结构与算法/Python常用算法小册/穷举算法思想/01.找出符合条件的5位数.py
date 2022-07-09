"""
打印出 符合条件的五位数.

这五位数分别是: 算法描述题.
则.
算法描述题 x 题 = 题题题题题题
其实就是
abcde x e = eeeeee
"""

for i in range(10000, 99999):
    a = i // 10000
    b = i % 10000 // 1000
    c = i % 10000 % 1000 // 100
    d = i % 10000 % 1000 % 100 // 10
    e = i % 10000 % 1000 % 100 % 10
    if e == 0:
        continue
    if int(str(a) + str(b) + str(c) + str(d) + str(e)) * a == int(str(e) * 6):
        print(int(str(a) + str(b) + str(c) + str(d) + str(e)))
