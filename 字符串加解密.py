#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：字符串加解密

描述
对输入的字符串进行加解密，并输出。

加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

解密方法为加密的逆过程。

数据范围：输入的两个字符串长度满足 1≤n≤1000  ，保证输入的字符串都是只由大小写字母或者数字组成

输入描述：
第一行输入一串要加密的密码
第二行输入一串加过密的密码

输出描述：
第一行输出加密后的字符
第二行输出解密后的字符

示例1
输入：

abcdefg
BCDEFGH
输出：

BCDEFGH
abcdefg
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125138757
"""

# 解题想法：不管加密解密，都变成顺序往后移一位


while True:
    try:
        s1 = input()
        s2 = input()
        res1 = ""
        res2 = ""
        l1 = "abcdefghijklmnopqrstuvwxyza"
        l2 = "01234567890"
        for i in s1:
            if i.lower() in l1:
                a = l1.index(i.lower())
                if i.islower():
                    res1 += l1[a + 1].upper()
                else:
                    res1 += l1[a + 1].lower()
            elif i in l2:
                b = l2.index(i)
                res1 += l2[b + 1]
        l3 = "zabcdefghijklmnopqrstuvwxyz"[::-1]
        l4 = "01234567890"[::-1]
        for i in s2:
            if i.lower() in l3:
                a = l3.index(i.lower())
                if i.islower():
                    res2 += l3[a + 1].upper()
                else:
                    res2 += l3[a + 1].lower()
            elif i in l4:
                b = l4.index(i)
                res2 += l4[b + 1]
        print(res1)
        print(res2)
    except Exception as e:
        #         print(e)
        break


