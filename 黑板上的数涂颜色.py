#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

华为OD机试题：黑板上的数涂颜色

题目描述：

疫情过后希望小学终于又重新开学了，3年2班开学第一天的任务是：将后面的黑板报重新制作
黑板上已经写上了N个正整数，同学们需要给这每个数分别上一种颜色，为了让黑板报既美观又有学习意义
老师要求同种颜色的所有数都可以被这个颜色中最小的那个数整除，现在帮小朋友们算算最少需要多少种颜色，给这N个数进行上色


输入描述：

第一行有一个正整数N，其中 1 <= n <=100
第二行有N个int型数，保证输入数据在[1,100]范围中，表示黑板上各个正整数的值


输出描述：

输出只有一个整数，为最少需要的颜色种数


示例

1.输入：

3
2 4 6
输出：1
说明：

所有数都能被2整除
2.输入：

4
2 3 4 9
输出：2
说明：

2与4涂一种颜色，4能被2整除
3与9涂另一种颜色，9能被3整除
不能涂同一种颜色
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125032488
"""


def func(n: int, l: list):
    # 解题思想：每次获取列表最小值，去除能被它整除的数；如果列表剩下一个元素，则结果加一，跳出循环
    res = 0
    ll = l.copy()  # 注意ll=l，会将ll与l指向同一个内存地址，所以使用copy()
    while len(l) > 0:
        if min(l) == 1:
            return 1
        if len(l) == 1:
            res += 1
            break
        else:
            a = min(l)
            res += 1
            for i in ll:
                if i % a == 0:
                    l.remove(i)
    return res


if __name__ == '__main__':
    print(func(4, [2, 3, 4, 9]))
