#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：最长回文子串

描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。

所谓回文串，指左右对称的字符串。

所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串

数据范围：字符串长度1≤s≤350

进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)

输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度

示例1
输入：

cdabbacc

输出：4
说明：abba为最长的回文子串
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125122259
"""


# #解题想法：如果是回文子串，首先该起始字符再子串中出现不止一次，那么找到它的对称的截止位置，
# 是否相同回文子串，是就比较长度
# 注：1.str.count()可以设置统计起始位置；2.try...except...要写成try:....except exception as e:print(e)，方便判断执行错误
#
# ————————————————
# 版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/cxh21627/article/details/125122259

def longestPalindrome(s: str) -> str:
    res = ''
    for i in range(len(s)):
        # 以 s[i] 为中心的最长回文子串
        s1 = palindrome(s, i, i)
        # 以 s[i] 和 s[i+1] 为中心的最长回文子串
        s2 = palindrome(s, i, i + 1)
        res = res if len(res) > len(s1) else s1
        res = res if len(res) > len(s2) else s2
    return res


def palindrome(s, l, r):
    # 防止索引越界
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # 双指针，向两边展开
        l -= 1
        r += 1
    # 返回以 s[l] 和 s[r] 为中心的最长回文串
    return s[l + 1:r]

if __name__ == '__main__':
    while True:
        try:
            s = input()
            res = longestPalindrome(s)
            print(len(res))
        except Exception as e:
            break
