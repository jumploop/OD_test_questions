#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：质数因子

描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围： 1≤n≤2×109+14

输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。

示例1
输入：

180
输出：2 2 3 3 5
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125073360
"""


def func():
    # 解题想法：取2~n^(0.5)之间的数，不断被n整除，并重新定义n，
    # 当数组不能增加时，就说明此时的n也是质数
    s = int(input())
    l = []
    flag = True
    while flag:
        a = len(l)
        for i in range(2, int(s ** 0.5) + 1):
            if s % i == 0:
                l.append(i)
                s = int(s / i)
                break
        if a == len(l):
            l.append(s)
            flag = False

    for i in l:
        print(i, end=" ")


if __name__ == '__main__':
    func()
