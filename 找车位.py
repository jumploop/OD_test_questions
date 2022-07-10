"""
【找车位】 停车场有一横排车位，0代表没有停车，1代表有车。至少停了一辆车在车位上，也至少有一个空位没有停车。

为了防剐蹭，需为停车人找到一个车位，使得距停车人的车最近的车辆的距离是最大的，返回此时的最大距离。

输入描述：

1、一个用半角逗号分割的停车标识字符串，停车标识为0或1，0为空位，1为已停车。

2、停车位最多100个。

输出描述：

输出一个整数记录最大距离。

示例1：

输入

1,0,0,0,0,1,0,0,1,0,1

输出

2
"""


def solution(s):
    arr = s.split(',')
    maxCount = 0
    for i in range(len(arr)):
        leftCount = 0
        rightCount = 0
        if arr[i] != '1':
            index = i
            while index > 0 and arr[index] == '0':
                leftCount += 1
                index -= 1
            index = i
            while index < len(arr) and arr[index] == '0':
                rightCount += 1
                index += 1
            count = min(leftCount, rightCount)
            maxCount = max(count, maxCount)
    print(maxCount)


if __name__ == "__main__":
    s = '1,0,0,0,0,1,0,0,1,0,1'
    solution(s)