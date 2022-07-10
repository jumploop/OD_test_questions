"""
对输入的单词进行字典序排序输出： 字典序定义

单词中字母比较不区分大小写，两个单词先以第一个字母作为排序的基准，如果第一个字母相同， 就用第二个字母为基准，如果第二个字母相同就以第三个字母为基准。依此类推，如果到某个字母不相同，字母顺序在前的那个单词顺序在前。
当一个短单词和一个长单词的开头部分都相同（即短单词是长单词从首字母开始的一部分），短单词顺序在前。
字母大小写不同的相同单词，只输出一次。
输入描述:

不超过255个字符中,单词间用空格进行分隔，为简单起见，单词不包含连字符，无其它标点符号输出描述:

输出排序后的单词，单词之间用空格隔开（最后不带空格），重复的单词只输出一次。 示例1 输入 Hello hello world 输出 Hello world 升序排序
"""


def dict_sort(arr):
    result = []
    for i in arr:
        if i.lower() not in map(str.lower, result):
            result.append(i)
    return sorted(result, key=str.lower)


if __name__ == '__main__':
    lists = ['Hello', 'hello', 'world']
    res = dict_sort(lists)
    print(' '.join(res))
