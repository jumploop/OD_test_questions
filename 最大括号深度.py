"""

现有一字符串仅由 ‘(’，’)’，’{’，’}’，’[’，’]'六种括号组成。

若字符串满足以下条件之一，则为无效字符串：

①任一类型的左右括号数量不相等；

②存在未按正确顺序（先左后右）闭合的括号。

输出括号的最大嵌套深度，若字符串无效则输出0。

0≤字符串长度≤100000

输入描述:

一个只包括 ‘(’，’)’，’{’，’}’，’[’，’]'的字符串

输出描述:

一个整数，最大的括号深度

示例1

输入

[]

输出

1

说明

有效字符串，最大嵌套深度为1

示例2

输入

([]{()})

输出

3

说明

有效字符串，最大嵌套深度为3

示例3

输入

(]

输出

0

说明

无效字符串，有两种类型的左右括号数量不相等

示例4

输入

([)]

输出 0

说明

无效字符串，存在未按正确顺序闭合的括号

示例5

输入

)(

输出

0

说明

无效字符串，存在未按正确顺序闭合的括号
"""

# 是否是有效滴字符串


def isValid(s: str) -> bool:
    # 是否是合法的字符串
    if len(s) % 2 == 1:
        return False
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


def main():
    arr = '([]{()})'
    rightMarkArr = [')',']','}']
    print(list(arr))
    deep = 0
    maxDeep = 0
    if not isValid(arr):
        return 0
    for ch in arr:
        if ch not in rightMarkArr:
            deep += 1
            maxDeep = max(deep, maxDeep)
        else:
            deep -= 1
    return maxDeep


if __name__ == '__main__':
    print(main())