#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：整数表达为连续自然数之和

题目描述：

一个整数可以由连续的自然数之和来表示，给定一个整数，计算该整数有几种连续自然数之和的表达式，并打印出每一种表达式。


输入描述：

一个目标整数t 1<= t <=1000


输出描述：

该整数的所有表达式和表达式的个数，如果有多种表达式，自然数个数最少的表达式优先输出
每个表达式中按自然数递增输出
在每个测试数据结束时，输出一行"Result:X"，其中X是最终的表达式个数


示例

输入：

9
输出：

9=9
9=4+5
9=2+3+4
Result:3
说明：

整数9有三种表达方法：
输入：

10
输出：

10=10
10=1+2+3+4
Result:2
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125017754
"""


def func(n):
    # 解题想法：现将“n=n”形式记录，再从1到1-9的一半+1每一个数为起点，循环找出累加和等于n的列表，
    # 对结果列表根据长度排序，打印

    res = 1
    k = 1
    l = [[n]]

    for i in range(1, int(n / 2) + 1):
        ll = [i]
        sum = i
        j = i + 1
        while j < n:
            sum += j
            if sum < n:
                ll.append(j)
                j += 1
            if sum == n:
                ll.append(j)
                l.append(ll)
                k += 1
                break
            if sum > n:
                break
    l.sort(key=len)  # key可输入方法名

    for i in l:
        i = list(map(str, i))
        a = "+".join(i)
        print(f"{n}={a}")

    print(f"Result:{k}")


def func2():
    # 解题想法2：因为按元素个数由小到大输出，那么从大往小走若干个元素的和是否等于m，即可

    m = int(input())
    res = []
    for i in range(m, 0, -1):
        # print(i)
        sum = 0
        l = []
        for j in range(i, m + 1):
            sum += j
            l.append(str(j))
            if sum == m:
                print(f"{m}=" + "+".join(l))
                res.append(l)
                break
            if sum > m:
                break

    print(f"Result:{len(res)}")


if __name__ == '__main__':
    func(9)
