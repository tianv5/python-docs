"""
描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列

输入描述：
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1
输入：
10.0.3.193
167969729
复制
输出：
167773121
10.3.3.193
"""


# ip_str = input()
# num = int(input())


def ip_print_int(ip_str):
    """
    输入 10.0.3.193
    输出 167773121
    """
    num_list = [int(i) for i in ip_str.split(".")]
    str_2 = ""
    for i in num_list:
        # 11000001 8位0、1
        tmp = str(bin(i)).replace("0b", '')
        tou = (8 - len(tmp)) * "0"
        tmp = tou + tmp
        str_2 += tmp
    int_num = int(str_2, 2)
    return int_num


def ip_print_str(n):
    # n_str = "1010000000000000001111000001"
    n_str = str(bin(n)).replace("0b", "")

    len_tou = 32 - len(n_str)
    n1 = n_str[:8 - len_tou]
    n2 = n_str[8 - len_tou:16 - len_tou]
    n3 = n_str[16 - len_tou:24 - len_tou]
    n4 = n_str[24 - len_tou:32 - len_tou]

    n1 = int(n1, 2)
    n2 = int(n2, 2)
    n3 = int(n3, 2)
    n4 = int(n4, 2)

    ip = f"{n1}.{n2}.{n3}.{n4}"
    return ip


ip_str = input()
num = int(input())
print(ip_print_int(ip_str))
print(ip_print_str(num))

