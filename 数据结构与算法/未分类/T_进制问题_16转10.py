"""
输入一个16进制的字符串。
输出10进制字符串，不同测试用\n隔开
"""

str_16 = str(input()).strip()
print(str(int(str_16, 16)))