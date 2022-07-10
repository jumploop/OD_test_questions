#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：数组和窗口

题目描述：

有一个N个整数的数组和一个长度为M的窗口。
窗口从数组内的第一个数开始滑动，直到窗口不能滑动为止。
每次滑动产生一个窗口 和窗口内所有数的和。
求窗口滑动产生的所有窗口和的最大值。


输入描述：

第一行输入一个正整数N，表示整数个数 0<N<100000。
第二行输入N个整数，整数取值范围 [-100,100]。
第三行输入正整数M，M代表窗口的大小，M<=100000 并<=N。


输出描述：

窗口滑动产生所有窗口和的最大值


示例

输入：

6
12 10 20 30 15 23
3
输出：

68
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125010356
"""


def func(n: int, l: list, m: int):
    res = -float('inf')
    for i in range(len(l) - m + 1):
        sum = 0
        for j in range(i, i + m):
            sum += l[j]
        res = max(sum, res)
    return res


if __name__ == '__main__':
    print(func(6, [12, 10, 20, 30, 15, 23], 3))
