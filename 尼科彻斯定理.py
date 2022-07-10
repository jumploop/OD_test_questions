#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：尼科彻斯定理

描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。

例如：

1^3=1

2^3=3+5

3^3=7+9+11

4^3=13+15+17+19

输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。

数据范围：1≤m≤100

进阶：时间复杂度：O(m)\O(m) ，空间复杂度：O(1)\O(1)

输入描述：
输入一个int整数

输出描述：
输出分解后的string

示例1
输入：

6
输出：31+33+35+37+39+41


————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125099911
"""


def func(m):
    # 解题想法：因为等价于m个数相加，所以m个数的平均数为m ** 2, 再根据m的奇偶，添加两边的数
    l = []
    a = m ** 3
    b = m ** 2
    if m % 2 == 1:
        l.append(b)
        for i in range(int((m - 1) / 2)):
            l.extend((b - (i + 1) * 2, b + (i + 1) * 2))
    else:
        l.extend((b + 1, b - 1))
        for i in range(int((m - 2) / 2)):
            l.extend((b - 1 - (i + 1) * 2, b + 1 + (i + 1) * 2))
    l.sort()
    l = list(map(str, l))
    res = "+".join(l)
    if a == eval(res):
        print(res)


if __name__ == '__main__':
    func(3)
