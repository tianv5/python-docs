"""
插入排序的话，可以将列表插入到一个空表中。
或
前n个是有序，后m个是待插入序列。
4,5,7,6,9,3
4,5,7 有序
6,9,3 待插入

刚才是的时候，把第一个元素当做有序序列，后面的是待插入序列~！
"""

import random

random_list = [random.randint(1, 20) for i in range(0, 20)]
list_len = len(random_list)

for i in range(1, list_len):
    j = 0
    is_swap = False # 优化
    # j为索引，有序
    # i为待插入的值的索引
    while j < i:  #
        # 比较 0,1 的值，从小到大排序的
        # 有序序列 从 0到j开始比较
        # 一直到 待插入的数据，比有序序列小，停止
        if random_list[j] > random_list[i]:
            is_swap = True # 除了此优化，还可以用二分查找等方法
            break
        j = j + 1  # 继续下一个比较
    if is_swap == True:
        continue
    tmp = random_list[i]  # 插入的值
    k = i  # 记录索引，一会会加减操作
    # 数据移动
    while k > j:
        random_list[k] = random_list[k - 1]
        k = k - 1
    # 插入数据
    random_list[k] = tmp
print(random_list)