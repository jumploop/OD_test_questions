#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

华为OD机试题：数独
数独是一个我们都非常熟悉的经典游戏，运用计算机我们可以很快地解开数独难题，现在有一些简单的数独题目，请编写一个程序求解。

如有多解，输出一个解

输入描述:

输入9行，每行为空格隔开的9个数字，为0的地方就是需要填充的。
输出描述:

输出九行，每行九个空格隔开的数字，为解出的答案。
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125056836
"""
"""

#解题想法：首先九宫格判断规则，横、竖、宫格内数字不重复，所以有三种判断方法，取交集看共享的是否
为一个，是一个就填写，但由于存在多解（且此时交集为两个元素），故增加试错机制，当发现零点个数没有
发生变化，便进行试验，并记录当前节点状态，后面如果发现零点的三种判断方法没有交集，便恢复状态，
并确认另外一个值是正确的
"""
import sys


def heng(i, j, ll):
    n = []
    for m in range(0, 9):
        if ll[i][m] != 0:
            n.append(ll[i][m])
    return list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(n))


def shu(i, j, ll):
    n = []
    for m in range(0, 9):
        if ll[m][j] != 0:
            n.append(ll[m][j])
    return list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(n))


def gong(i, j, ll):
    m1 = i // 3
    m2 = j // 3
    n = []
    for a in range(m1 * 3, m1 * 3 + 3):
        for b in range(m2 * 3, m2 * 3 + 3):
            if ll[a][b] != 0:
                n.append(ll[a][b])
    return list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(n))




if __name__ == '__main__':

    ll = [
            [0, 0, 8, 7, 1, 9, 2, 4, 5],
            [9, 0, 5, 2, 3, 4, 0, 8, 6],
            [0, 7, 4, 8, 0, 6, 1, 0, 3],
            [7, 0, 3, 0, 9, 2, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 6, 1, 4, 0, 3, 5, 2, 9],
            [4, 0, 0, 0, 2, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0, 0, 7, 0],
            [1, 0, 7, 0, 6, 8, 0, 5, 0],
        ]

    while True:
        isCon = True
        # ll = []
        # for i in range(9):
        #     tp = sys.stdin.readline().strip()
        #     if not tp:
        #         isCon = False
        #         break
        #     tp = [int(i) for i in tp.split(' ')]
        #     ll.append(tp)
        if isCon == False:
            break
        dd = []
        q = 0
        r = 0
        w = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if ll[i][j] == 0:
                    dd.append([i, j])
        while len(dd) > 0:
            ko = len(dd)
            for r in dd:
                res = []
                i = r[0]
                j = r[1]
                h1 = heng(i, j, ll)
                s1 = shu(i, j, ll)
                g1 = gong(i, j, ll)
                for o in h1:
                    if o in s1 and o in g1:
                        res.append(o)
                if len(res) == 0:
                    dd = dl
                    ll[q][r] = w
                    dd.remove([i, j])
                    continue
                if len(res) == 1:
                    ll[i][j] = res[0]
                    dd.remove([i, j])
                else:
                    continue
            if ko == len(dd):
                res = []
                i = dd[0][0]
                j = dd[0][1]
                h1 = heng(i, j, ll)
                s1 = shu(i, j, ll)
                g1 = gong(i, j, ll)
                for o in h1:
                    if o in s1 and o in g1:
                        res.append(o)
                ll[i][j] = res[0]
                dl = dd.copy()
                q = i
                r = j
                w = res[1]
                dd.remove([i, j])

        for x in ll:
            x = list(map(str, x))
            y = " ".join(x)
            print(y)
