#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
拼接url

题目描述：

给定一个url前缀和url后缀,通过,分割 需要将其连接为一个完整的url
如果前缀结尾和后缀开头都没有/，需要自动补上/连接符
如果前缀结尾和后缀开头都为/，需要自动去重
约束：不用考虑前后缀URL不合法情况


输入描述：

url前缀(一个长度小于100的字符串) url后缀(一个长度小于100的字符串)


输出描述：

拼接后的url


示例

1.输入：/acm,/bb
输出：/acm/bb
2.输入：/abc/,/bcd
输出：/abc/bcd
3.输入：/acd,bef
输出：/acd/bef
4.输入：,
输出：/
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125029547
"""


def func(s):
    # 解题想法：就分三种情况，前后都有/，前后有一个/，前后都没有/

    l = s.split(",")
    res = ""

    if l[0].endswith("/") and l[1].startswith("/"):
        res = l[0] + l[1][1:]
        return res
    if l[0].endswith("/") or l[1].startswith("/"):
        res = l[0] + l[1]
        return res
    if not l[0].endswith("/") and not l[1].startswith("/"):
        res = l[0] + "/" + l[1]
        return res


if __name__ == '__main__':
    print(func('/acm,/bb'))
