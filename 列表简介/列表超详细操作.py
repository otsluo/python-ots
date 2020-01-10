#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ots_luo
# Time：2020-01-09


#-------------列表------------
list_1 = ['中文', "English",123]
list_2 = [1, 2, 3, 4, 5 ]
list_3 = ["a", "b", "c", "d"]
print(list_1)
print(list_2)
print(list_3)


#---------------------简单的索引方式访问列表中元素---------------
#访问下面索引的第一和第三的位置
list_2 = [1, 2, 3, 4, 5 ]
print(list_2[1])

list_3 = ["a", "b", "c", "d"]
print(list_3[1])
print(list_3[3])
#访问最后一个列表元素：
print(list_3[-1])

#------------修改、添加和删除元素-------------
#修改列表元素
list_3 = ["a", "b", "c", "d"]
list_3[2] = 'aaa'
print(list_3)

#------------添加列表元素---------------
# 末尾添加元素
list_3 = ["a", "b", "c", "d"]
print('添加前',list_3)
list_3.append('ots')
print('添加后',list_3)

# 空列表添加元素
list_4 = []
list_4.append('aaa')
list_4.append('bbb')
list_4.append('ccc')
print(list_4)


#列表中插入元素
list_3 = ["a", "b", "c", "d"]
list_3.insert(2,'ots')
print(list_3)


#使用del删除列表的元素
list_3 = ["a", "b", "c", "d"]
del list_3[2]
print(list_3,'删除2位置')
#del list_3
#print(list_3,'删除全部')

#使用方法pop() 删除元素
list_4  = ['aaa', 'bbb', 'ccc','ddd']
list_5 = list_4.pop()
print(list_4)
print(list_5)

#使用remove根据值删除元素
list_5  = ['aaa', 'bbb', 'ccc','ddd']
list_5.remove('aaa')
print(list_5)

#------------------组织列表---------------
# 使用方法sort()对列表进行永久排序
# 默认排序
list_7  = ['c', 'd', 'b','a']
list_7.sort()
print(list_7)
# 反向排序
list_7  = ['c', 'd', 'b','a']
list_7.sort(reverse=True)
print(list_7)

# 使用函数sorted() 对列表进行临时排序
list_7  = ['c', 'd', 'b','a']
print(sorted(list_7))
print(sorted(list_7,reverse=True))

# 使用函数len（）获取列表长度
list_7  = ['c', 'd', 'b','a']
print(len(list_7))
