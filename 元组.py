#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ots-luo
# Time：2020-02-22

#--------定义元组----------
yuanzu =('ots安全','ots指南针','ots建站')
print(yuanzu)

#--------测试修改元组----------
yuanzu1 =('ots安全','ots指南针','ots建站')
print(yuanzu1)
#yuanzu1[0] = 3


#--------遍历元组---------
yuanzu2 =('ots安全','ots指南针','ots建站')
for i in yuanzu2:
    print(i)

#--------修改元素变量---------
yuanzu3 =('ots安全','ots指南针','ots建站')
print('未修改',yuanzu3)
for i in yuanzu3:
    print(i)

yuanzu3 =(1,2,3)
print('修改后：',yuanzu3)
for q in  yuanzu3:
    print(yuanzu3)



