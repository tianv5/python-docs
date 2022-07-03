"""
冒泡排序.

重点.
比较相邻元素,比较大小后交换位置.
<位置1, 位置2, 位置3, 位置4, 位置5>
比较
<1,2> <2,3> <3,4> <4,5>
第一轮结束,5号位置一定是最大的.

第2轮, 最大的两个<4,5>号位排序完成.
第n轮,排序结束.


编写思路,先写交换位置的
for i in range(len(num_list) - 1):
    # 交换位置
    if num_list[i] > num_list[i + 1]:
        num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
print(num_list)


再写遍历times次.
for times in range(1, len(num_list)):
    # 第n轮(times)
    for i in range(len(num_list) - times):
        # 交换位置
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    print(num_list)

"""


def bubble_sort(num_list):
    for times in range(1, len(num_list)):
        # 第n轮(times)
        for i in range(len(num_list) - times):
            # 交换位置
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        # 每轮结束后的列表
        print(num_list)


if __name__ == '__main__':
    num_list = [9, 8, 5, 5, 6, 9, 5, 4, 6, 3, 2, 3, 2, 1]
    bubble_sort(num_list)
