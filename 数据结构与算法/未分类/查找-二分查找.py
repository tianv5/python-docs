"""
首先列表必须是有序的.

"""

def binary_search(list, item):
    # 列表的头和尾，代表着数组范围的最小和最大
    low = 0
    high = len(list) - 1

    # 当找到item的时候，low是小于high，也有可能相等
    while low <= high:

        mid = (low + high) // 2
        print(mid)

        # 取数组的中间值
        guess = list[mid]

        # 如果中间值等于索引值，那么就返回中间值的下标
        if guess == item:
            return mid

        # 如果中间值>索引值，因为不包含中间值，所以最大范围high=中间值的下标往左移1位
        if guess > item:
            high = mid - 1

        # 如果中间值<索引值，因为不包含中间值，所以最小范围low=中间值的下标往右移1位
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
index = binary_search(my_list, 3)