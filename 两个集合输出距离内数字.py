#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：两个集合输出距离内数字

题目描述：

同一个数轴x有两个点的集合A={A1,A2,…,Am}和B={B1,B2,…,Bm}
A(i)和B(j)均为正整数
A、B已经按照从小到大排好序，AB均不为空
给定一个距离R 正整数，列出同时满足如下条件的(A(i),B(j))数对：
1.A(i)<=B(j)
2.A(i),B(j)之间距离小于等于R
3.在满足1，2的情况下每个A(i)只需输出距离最近的B(j)
4.输出结果按A(i)从小到大排序


输入描述：

第一行三个正整数m n R
第二行m个正整数 表示集合A
第三行n个正整数 表示集合B
输入限制 1<=R<=100000，1<=n,m<=100000，1<= A(i),B(j) <= 1000000000


输出描述：

每组数对输出一行 A(i)和B(j)
以空格隔开


示例

输入：

4 5 5
1 5 5 10
1 3 8 8 20

输出：

1 1
5 8
5 8
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125017462
"""


def func(s: str, sl1: str, sl2: str):
    # 解题想法：由于已经排序，找到第一个符合条件的就输出结果，否则就跳过

    m = int(s.split(" ")[2])
    l1 = list(map(int, sl1.split(" ")))
    l2 = list(map(int, sl2.split(" ")))

    for i in l1:
        for j in l2:
            if j >= i and j - i <= m:
                print(f"{i} {j}")
                break


if __name__ == '__main__':
    func('4 5 5', '1 5 5 10', '1 3 8 8 20')
