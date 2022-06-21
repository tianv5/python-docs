"""
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足1<=n<=100

注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。

对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

输入例子1:
3
10
81
0


输出例子1:
1
5
40
"""


def huan_ping(n):
    # 总共兑换的瓶子
    total = 0
    while True:
        tmp_total = n // 3
        kong_ping = n % 3
        # 当前可剩余的空瓶
        n = tmp_total + kong_ping
        # 已经换到的瓶子数量
        total += tmp_total

        if n < 2:
            break
        elif n == 2:
            total += 1
            break
    return total


input_list = []

while True:
    num = int(input())
    if num == 0:
        break
    input_list.append(num)

for num in input_list:
    x = huan_ping(num)
    print(x)
