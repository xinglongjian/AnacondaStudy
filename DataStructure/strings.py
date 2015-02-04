# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:55:55 2015

@author: zwl
"""
#可以是单引号或双引号
s='hello'
print(s)
s="hello"
print(s)

#如果字符串内有引号可以使用双引号或转义字符
s="Dot's Worry"
print(s)
s='Dot\'s Worry'
print(s)

s="c:\\dd\\"
print(s)

#''' 和"""用于多行字符串
s='''fad
asdfasdfa
afdadfadf'''
print(s)

s="""sdfasdf
asdfasd
afa"""
print(s)