# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:06:29 2015

@author: zwl
"""

#创建空字典
d={}
print(d)
print(type(d))

d={"d":"33","33":"344"}
print(d)
#接收一系列key-value组合
m={("d","33"),("33","344")}
d=dict(m)
print(d)

