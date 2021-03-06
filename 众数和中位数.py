#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：众数和中位数

题目描述：

众数是指一组数据中出现次数多的数，众数可以是多个。
中位数是指把一组数据从小到大排列，最中间的那个数；如果这组数据的个数是奇数，那最中间那个就是中位数；如果这组数据的个数为偶数，那就把中间的两个数之和除以2就是中位数。
查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数。


输入描述：

输入一个一维整型数组，数组大小取值范围 0<n<1000
数组中每个元素取值范围， 0<e<1000


输出描述：

输出众数组成的新数组的中位数。


示例

1.输入：

10 11 21 19 21 17 21 16 21 18 16

输出：21

2.输入：

2 1 5 4 3 3 9 2 7 4 6 2 15 4 2 4

输出：3

3.输入：

5 1 5 3 5 2 5 5 7 6 7 3 7 11 7 55 7 9 98 9 17 9 15 9 9 1 39
输出：7
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125012309
"""
from collections import Counter


def func(l: list):
    # 解题想法：先通过列表记录l的众数，排序后，然后再根据奇偶返回中位数
    c = Counter(l)
    print(c)
    ll = []
    m = max(c.values())
    for k, v in c.items():
        if v == m:
            ll.append(k)
    ll.sort()
    if len(ll) % 2 == 1:
        return ll[int((len(ll) - 1) / 2)]  # python整除也会自带一位小数点
    return (ll[int(len(ll) / 2)] + ll[int(len(ll) / 2 - 1)]) // 2


if __name__ == '__main__':
    print(func([10, 11, 21, 19, 21, 17, 21, 16, 21, 18, 16]))
    print(func([2, 1, 5, 4, 3, 3, 9, 2, 7, 4, 6, 2, 15, 4, 2, 4]))
    print(func([5, 1, 5, 3, 5, 2, 5, 5, 7, 6, 7, 3, 7, 11, 7, 55, 7, 9, 98, 9, 17, 9, 15, 9, 9, 1, 39]))
