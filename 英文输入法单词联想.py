#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

华为OD机试题：英文输入法单词联想

题目描述：

主管期望你来实现英文输入法单词联想功能。


需求如下：依据用户输入的单词前缀， 从已输入的英文语句中联想出用户想输入的单词， 按字典序输出联想到的单词序列， 如果联想不到， 请输出用户输入的单词前缀。
注意：

1.英文单词联想时区分大小写

2.缩略形式如"don’t" 判定为两个单词 "don"和 "t"输出的单词序列不能有重复单词且只能是英文单词，不能有标点符号。


输入描述：

输入两行

首行输入一段由英文单词word和标点构成的语句str

接下来一行为一个英文单词前缀pre

0 < word.length() <= 20

0 < str.length <= 10000

0 < pre <=20

输出描述：

输出符合要求的单词序列或单词前缀，存在多个时，单词之间以单个空格分割


示例

输入：

I love you
He
输出：He
说明：

用户已输入单词语句"I love you",中提炼出"I",“love”,“you"三个单词 接下来用户输入"He” ，从已经输入信息中无法联想到符合要求的单词，所以输出用户输入的单词前缀。
输入：

The furthest distance in the world,Is not between life and death,But when I stand in front or you,Yet you don’t know that I love you.
f
输出：

front furthest
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125002240
"""
import re


def func(s1, s2):
    pat = re.compile(r'[\W]+')
    arr = pat.split(s1)
    result = []
    for i in arr:
        if i not in result:
            if i.startswith(s2):
                result.append(i)
    if result:
        result.sort()
        print(' '.join(result))
    else:
        print(s2)


if __name__ == '__main__':
    func('I love you', 'He')
    func(
        'The furthest distance in the world,Is not between life and death,But when I stand in front or you,Yet you don’t know that I love you.',
        'f')
