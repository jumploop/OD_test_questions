#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

华为OD机试题：走方格的方案数

描述


请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。

注：沿棋盘格之间的边缘线行走

数据范围： 1≤n,m≤8

输入描述：
输入两个正整数n和m，用空格隔开。(1≤n,m≤8)

输出描述：
输出一行结果

示例1
输入：

2 2
输出：6

理解：


————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125099331
"""


def func():
    # 解题想法：动态规划，如果这个点在边缘上，根据不能往回走原则，通向它的路只有一条；如果不在边缘，则它等于上面的节点的路条数+左面的节点的条数
    s = "3 3"
    # s = input().split(" ")
    l = list(map(int, s.split(" ")))
    a = l[0]
    b = l[1]
    ll = []

    for i in range(0, l[0] + 1):
        ll.append([1])
        for j in range(0, l[1]):
            ll[i].append(0)
    for i in range(0, b + 1):
        ll[0][i] = 1
    print(ll)
    for i in range(1, a + 1):  # hang
        for j in range(1, b + 1):  # lie
            ll[i][j] = ll[i][j - 1] + ll[i - 1][j]
    print(ll[a][b])


if __name__ == '__main__':
    func()
