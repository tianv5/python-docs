"""
3
10
81
0
"""
import sys

num_list = []
for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    num_list.append(n)

print(num_list)
for n in  [3,10,81]:

    total = 0
    while True:
        duihuan = n // 3
        total += duihuan
        shengyu = n % 3
        n = shengyu + duihuan
        if n < 2:
            break
        elif n == 2:
            total += 1
            break
    print(total)