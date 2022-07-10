#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目描述：

有N个正整数组成的一个序列，给定一个整数sum
求长度最长的的连续子序列使他们的和等于sum
返回次子序列的长度，如果没有满足要求的序列 返回-1
备注：

输入序列仅由数字和英文逗号构成，数字之间采用英文逗号分割
序列长度 1<=N<=200，输入序列不考虑异常情况
由题目保证输入序列满足要求


示例

1.输入：

1,2,3,4,2
6
输出：3
解析：1,2,3和4,2两个序列均能满足要求，所以最长的连续序列为1,2,3 因此结果为3
2.输入：

1,2,3,4,2
20
输出：-1
解释：没有满足要求的子序列，返回-1
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125044027
"""


def func(l: list, k: int):
    # 解题想法：连续子序列，所以不能排序，从头开始计算，如果与目标值相等，则记录
    # 最后对记录结果按长度排序
    res = []
    for i in range(len(l)):
        total = 0
        j = i
        while j < len(l):
            total += l[j]
            j += 1
            if total == k:
                tmp = l[i:j]
                res.append(tmp)
            if total > k:
                break
    if not res:
        print(-1)
    else:
        result = sorted(res, key=len, reverse=True)
        print(len(result[0]))


if __name__ == "__main__":
    func(l=[1,2,3,4,2], k=6)
