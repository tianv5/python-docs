"""
假设商店老板 需要找零, n元钱.

100 50 20 5 1元

如何使得所需钱币的数量最少
"""

z = [100, 50, 20, 5, 1]


def change(n):
    # 找的零钱 五张面值的个数 [0,0,0,0,0]
    m = [0 for _ in range(len(z))]
    for i, money in enumerate(z):
        m[i] = n // money
        n = n % money
    return m, n


if __name__ == '__main__':
    x, y = change(376)
    print("找的钱", x)
    print("找不开的", y)
