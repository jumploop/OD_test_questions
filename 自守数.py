#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：自守数

描述
自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数

数据范围： 1≤n≤10000

输入描述：
int型整数

输出描述：
n以内自守数的数量。

示例1
输入：

6
输出：4

说明：有0，1，5，6这四个自守数

示例2
输入：

1
输出：2

说明：

有0, 1这两个自守数
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125098584
"""


def func(n):
    return sum(bool(str(i ** 2).endswith(str(i))) for i in range(n + 1))


def func2(n):
    # 解题想法：”abcd“[-2:]=”cd“，既右一为 - 1
    total = 0
    for i in range(n + 1):
        a = str(i ** 2)
        b = str(i)
        if a[-len(b):] == b:
            total += 1
    return total


if __name__ == '__main__':
    print(func(1))
