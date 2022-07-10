#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：求最大连续bit数

描述
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

数据范围：数据组数：1\le t\le 5\1≤t≤5 ，1\le n\le 500000\1≤n≤500000

进阶：时间复杂度：O(logn)\O(logn) ，空间复杂度：O(1)\O(1)

输入描述：
输入一个int类型数字

输出描述：
输出转成二进制之后连续1的个数

示例1
输入：

200
输出：2

说明：200的二进制表示是11001000，最多有2个连续的1。
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125100193
"""


def func(s: str):
    # 解题想法：先转化为二进制，再转化为字符，再统计连续”1“的个数
    n = int(s)
    b = bin(n)
    res = 0
    m = 0
    for i in range(len(b)):
        if b[i] == '1':
            m += 1
            res = max(res, m)
        else:
            m = 0
    return res


if __name__ == '__main__':
    print(func(input()))
