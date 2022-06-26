def lengthOfLIS(n, nums):
    if not nums:
        return 0
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


n = int(input())  # 输入数组长度
s = input().split(" ")  # 输入代表数组的字符串
nums = [int(s[i]) for i in range(len(s))]
print(lengthOfLIS(n, nums))