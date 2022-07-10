#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：字符统计

描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。

数据范围：字符串长度满足 1≤len(str)≤1000

输入描述：
一个只包含小写英文字母和数字的字符串。

输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。

示例1
输入：

aaddccdc
输出：cda

说明：样例里，c和d出现3次，a出现2次，但c的ASCII码比d小，所以先输出c，再输出d，最后输出a.


————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125112870
"""



while True:
    # 解题思想：dict中排序
    try:
        s = input()
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        c = sorted(sorted(d.items(), key=lambda x: x[0]), key=lambda y: y[1], reverse=True)
        res = "".join(i[0] for i in c)
        print(res)
    except:
        break
