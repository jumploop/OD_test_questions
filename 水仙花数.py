#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
水仙花数

所谓的水仙花数是指一个n位的正整数其各位数字的n次方的和等于该数本身

例如例如153=1^3+5^3+3^3,153是一个三位数,153是一个三位数

输入描述：

第一行输入一个整数N，表示N位的正整数N在3-7之间包含3,7

第二行输入一个正整数M，表示需要返回第M个水仙花数

输出描述：

返回长度是N的第M个水仙花数，个数从0开始编号

若M大于水仙花数的个数返回最后一个水仙花数和M的乘积

若输入不合法返回-1

示例

输入：

3

0

输出：

153

说明：

153是第一个水仙花数

输入：

9

1

输出

-1

"""


def shui(n):
    if 3 <= n <= 7:
        arr = []
        for i in range(10 ** (n - 1), 10 ** n):
            sum = 0
            x = i
            # m=list(str(i))
            # for j in m:
            #     sum += int(j)**n
            while x:
                bit = x % 10
                sum += pow(bit, n)
                x = (x // 10)
            if sum == i:
                # print(i)
                arr.append(i)
        if M > len(arr):
            print(arr[len(arr) - 1] * M)
        else:
            print(arr[M])
    else:
        print(-1)


if __name__ == "__main__":
    N = 7
    M = 3
    shui(N)
