# 输入正整数n
n = int(input())

dp = [0] * (n + 1)
# 初始化0 1 菲波那切数列数
dp[1] = 1

# 斐波那契数是 [0,1,1,2,3,5]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
