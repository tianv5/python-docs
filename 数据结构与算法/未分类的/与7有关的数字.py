n = int(input().strip())

num = 0

for i in range(1, n+1):
    if i % 7 == 0:
        num += 1
    elif '7' in str(i):
        num += 1

print(num)

