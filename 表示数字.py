#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：表示数字

描述
将一个字符中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。

数据范围：字符串长度满足  1≤n≤100

输入描述：
输入一个字符串

输出描述：
字符中所有出现的数字前后加上符号“*”，其他字符保持不变

示例1
输入：

Jkdi234klowe90a3
输出：

Jkdi*234*klowe*90*a*3*
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125098496
"""

import re


def func(s: str):
    # 解题想法：判断当前位置是否为数字，再根据位置来具体放”*“，
    l = list(s)
    res = ""
    for i in range(len(s)):
        if l[i].isnumeric():
            if i == 0 or not l[i - 1].isnumeric():
                res = f"{res}*{l[i]}"
            if i > 0 and l[i - 1].isnumeric():
                res = res + l[i]
            if i == len(l) - 1:
                res = f"{res}*"
        elif i == 0 or i != 0 and not l[i - 1].isnumeric():
            res = res + l[i]
        else:
            res = f"{res}*{l[i]}"
    return res


if __name__ == '__main__':
    print(func('Jkdi234klowe90a3'))
    pat = re.compile(r'(\d+)')
    ret = pat.sub(r'*\1*', 'Jkdi234klowe90a3')
    print(ret)
