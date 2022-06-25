"""

给定
"""

n = int(input().strip())
data = list(map(int, input().strip().split()))


# n = 8
# data = [1, -2, 3, 10, -4, 7, 2, -5]
#
# dp = [0 for i in range(n)]
# dp[0] = data[0]
#
# for i in range(1, n):
#     if dp[i - 1] + data[i] > data[i]:
#         dp[i] = dp[i - 1] + data[i]
#     else:
#         dp[i] = data[i]
# print(dp)
# print(max(dp))


dp = [0 for i in range(n)]
dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i],data[i])

print(max(dp))