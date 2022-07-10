# 计算一维数组男生相连最大值
def sameArr(arr):
    maxLen = 0
    left = 0
    right = 0
    while right < len(arr)-1:
        right += 1
        if arr[left] == arr[right] and arr[right] == 'M':
            maxLen = max(right - left + 1, maxLen)
        else:
            left = right
    return maxLen


def main():
    maxLen = 0
    arr = [['F', 'M', 'M', 'F'], ['F', 'M', 'M', 'F'], ['M', 'M', 'F', 'M']]
    #  横的
    for i in arr:
        maxLen = max(sameArr(i), maxLen)
    #  竖的
    nums = len(arr[0])
    for j in range(nums):
        newArr = []
        for i in arr:
            newArr.append(i[j])

        maxLen = max(sameArr(newArr), maxLen)

    #  对角
    record = {}
    for i in range(len(arr)):
        for j in range(nums):
            key = j + i
            if key not in record:
                record[key] = []
            record.get(key).append(arr[i][j])

    for i, nums in record.items():
        maxLen = max(sameArr(nums), maxLen)

    print(maxLen)


if __name__ == '__main__':
    # female/male ???这题应该是这个意思 M就是男吧 反对角线咋算，求大神指点
    main()
