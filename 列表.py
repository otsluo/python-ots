#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ots_luo
# Time： 2020-01-09

#-------------列表
list_1 = ['中文', "English",123]
list_2 = [1, 2, 3, 4, 5 ]
list_3 = ["a", "b", "c", "d"]
print(list_1)
print(list_2)
print(list_3)
#---------------------索引--------------------
computer = ['cpu','显卡','鼠标','键盘','内存条','显示器','机箱','硬盘','主板']
print(computer[0])
print(computer[-1])
#---------------切片-------------
list_1 =[1,2,3,4,5,6,7,8,9]
print(list_1[::1])
print(list_1[::-1])
print(list_1[-1:-1])
print(list_1[-1:1:-1])