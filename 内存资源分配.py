#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
华为OD机试题：内存资源分配

题目描述：

有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源，用户会进行一系列内存申请，需要按需分配内存池中的资源，返回申请结果成功失败列表。
分配规则如下：
分配的内存要大于等于内存申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用。
需要按申请顺序分配，先申请的先分配。
有可用内存分配则申请结果为true，没有可用内存分配则返回false。
注：不考虑内存释放。

输入描述:

第一行为内存池资源列表，包含内存粒度数据信息，粒度数据间用逗号分割，一个粒度信息内部用冒号分割，冒号前为内存粒度大小，冒号后为数量。资源列表不大于1024，每个粒度的数量不大于4096。

第二行为申请列表，申请的内存大小间用逗号分隔。申请列表不大于100000。

如：

   64:2,128:1,32:4,1:128
   50,36,64,128,127


输出描述:

输出为内存池分配结果。

如：true,true,true,false,false



示例

输入：

  64:2,128:1,32:4,1:128
  50,36,64,128,127

输出：true,true,true,false,false
说明：

内存池资源包含：64K共2个、128K共1个、32K共4个、1K共128个的内存资源；

针对50,36,64,128,127的内存申请序列，分配的内存依次是：64,64,128,NULL,NULL,

第三次申请内存时已经将128分配出去，因此输出结果是：

true,true,true,false,false
————————————————
版权声明：本文为CSDN博主「CoCo_2022」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/cxh21627/article/details/125012013
"""


def func(s: str, l: list):
    res = []
    ll = []
    ls = s.split(',')
    for i in ls:
        tmp = i.split(':')
        for j in range(int(tmp[1])):
            ll.append(int(tmp[0]))
    for x in l:
        lll = []
        for k in ll:
            if k >= x:
                lll.append(k)
        lll.sort()
        if lll:
            res.append(True)
            ll.remove(lll[0])
        else:
            res.append(False)
    return res


if __name__ == '__main__':
    print(func('64:2,128:1,32:4,1:128', [50, 36, 64, 128, 127]))
