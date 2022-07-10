#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

华为OD机试题：最大最小N个数的和


题目描述：

给定一个数组，编写一个函数来计算它的最大N个数与最小N个数的和。你需要对数组进行去重。

题目说明：

数组中数字范围[0, 1000]
最大N个数与最小N个数不能有重叠，如有重叠，输入非法返回-1
输入非法返回-1


输入描述：

第一行输入M， M标识数组大小
第二行输入M个数，标识数组内容
第三行输入N，N表达需要计算的最大、最小N个数


输出描述：

输出最大N个数与最小N个数的和。

示例

1.输入：

5
95 88 83 64 100
2
输出：342
说明：最大2个数[100,95],最小2个数[83,64], 输出为342

输入：

5
3 2 3 4 2 2
2
输出：-1
说明：最大2个数[4,3],最小2个数[3,2], 有重叠输出为-1
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125001474
"""


def func(m: int, l: list, n: int):
    # 解题想法：先用set去重，再排序，再取前后n个元素判断是否有交集，再求和
    # set无序，且无排序方法
    ll = list(set(l))
    ll.sort()
    # 注意l可能存在重复元素，所以不能用m-n
    if len(set(ll[:n]) - set(ll[len(ll) - n:])) != n:
        return -1
    sum = 0
    for i in range(n):
        sum += ll[i]
    ll.reverse()
    for i in range(n):
        sum += ll[i]
    print(sum)
    return sum


if __name__ == '__main__':
    print(func(5, [95, 88, 83, 64, 100], 2))
