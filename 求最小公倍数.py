#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：求最小公倍数

描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

数据范围：1≤a,b≤100000

输入描述：
输入两个正整数A和B。

输出描述：
输出A和B的最小公倍数。

示例1
输入：

5 7
输出：35

示例2
输入：

2 4
输出：4
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125122953
"""


# 解题想法：从最小的数累加到第一个能被最大数整除的数字

def func(a, b):
    c = min(a, b)
    print(c)
    while True:
        if c % a == 0 and c % b == 0:
            print(c)
            break
        c += 1


# while True:
#     try:
#         l = list(map(int, str(input()).split(" ")))
#         a = min(l)
#         b = max(l)
#         for i in range(a, a * b + 1, a):
#             if i % b == 0:
#                 print(i)
#                 break
#     except Exception as e:
#         # print(e)
#         break

if __name__ == "__main__":
    func(2, 4)
