"""

查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

数据范围：字符串长度1<= length <= 300
进阶：时间复杂度：O(n3) ，空间复杂度：O(n)

输入描述：
输入两个字符串

输出描述：
返回重复出现的字符


输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw
复制
输出：
jklmnop
"""

n = input()
m = input()

if len(n) > len(m):
    max_str = n
    min_str = m
else:
    max_str = m
    min_str = n


"""
a = "abcde"
b = "asdafabcdevf
print(a[4:5])

a[:5] n   5
a[:4] a[1:5]  4
a[:3] a[1:4] a[2:5]  3
a[:2] a[2:4] a[3:5]  2
a[:1] a[2:3] a[3:4] a[4:5] 1
"""


# max_str = "abcsafjklmnopqrstuvw"
# min_str = "abcdefghijklmnop"
length = len(min_str)


# 倒叙输出？'
flag = False
max_output = None

for x in range(length):
    l = length - x
    if flag:
        break

    for i in range(length):

        if i + l > length:
            break
        max_output = min_str[i:i + l]
        if max_output in max_str:
            flag = True
            break
print(max_output)