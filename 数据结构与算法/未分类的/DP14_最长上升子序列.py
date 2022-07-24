def lengthOfLIS(n, nums):
    if not nums:
        return 0
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            """ 
            计算以第i个为结尾的,最长子序列
            x[0:j] + x[i]组成的串,最长就是 dp[j] 或者 dp[j] + 1，条件就行x[j] 和 x[i] 的大小
            """
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


n = int(input())  # 输入数组长度
s = input().split(" ")  # 输入代表数组的字符串
nums = [int(s[i]) for i in range(len(s))]
print(lengthOfLIS(n, nums))