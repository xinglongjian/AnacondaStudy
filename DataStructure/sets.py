# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:06:02 2015

@author: zwl
"""
#set 是一个没有重复元素的无序集合，只能包含任何不可变类型元素，
#如integer，float，string，tuple，但list和set不行
#与list相比，set对判断元素是否存在该集合中的方法做了优化
#是基于一种hashtable的数据结构

#创建一个空集合
s=set()
print(s)
print(len(s))
#s={} 不嫩用此方式创建，此方式创
#如果传入一个可迭代的参数，会自动转为set
s=set('hello')
print(s)


s={12,232,312,12}
print(s)
s={12.2,232.1,312.3}
print(s)
s={'12','232','312'}
print(s)
s={('12','232'),'312'} #tuple
print(s)
#s={[2,1],[3,23]}
#print(s)
#s={{2,1},{3,23}}
#print(s)



#frozenset用于构建不可变集合
fs=frozenset({'2','3'})
print(fs)