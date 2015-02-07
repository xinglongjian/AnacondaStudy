# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 16:17:36 2015

@author: zwl
"""

#Logical Operators
print('Logical Operators')
print(not True)
print(True and False)
print(True or False)
print('')

#Equality Operators
print('Equality Operators')
a=None
print(a is None)
print(a is not None)
print(a == None)
print(a!=None)

#Comparison Operators
print('Comparison Operators')
print(4>3)
print(3<5)
print('w'<='w')
print('q'>='w')

#Arithmetic Operators(+,-,*,/,//,%)
print('Arithmetic Operators')
q=11//5 #返回整数 2
print(q)
q=11%5 #返回余数1
print(q)
q=11/5 #返回float结果2.2
print(q)

#Bitwise Operators
print('Bitwise Operators')
print(~1)# -2 ~x=-(x+1)
print(1&3)
print(1|3)
print(2^2)
print(2<<2)

#Sequence Operators 
#python内置的序列类型（str, tuple,and list）都支持这些操作

s='hello'
t=(1,2,3,4,5)
l=[2,3,4,5,6]
#s[j] element at index j 
print(s[0])#h
print(t[0])#1
print(l[0])#2

#s[start:stop] slice including indices [start,stop) 
print(s[1:3])#el
print(t[1:3])#(2,3)
print(l[1:3])#[3,4]

#s[start:stop:step] slice including indices start, start + step, start + 2 step,...,up to but not equalling or stop 
print(s[0:5:2])#hlo
print(t[0:5:2])#(1,3,5)
print(l[0:5:2])#[2,4,6]

#s+t concatenation of sequences 
ss='world'
tt=(6,7)
ll=[7,8]
print(s+ss)
print(t+tt)
print(l+ll)

#k*s shorthand for s + s + s + ...(k times) 
print(3*s)
print(3*t)
print(3*l)

#val in s containment check ,val not in s non-containment check 
print('t' in s) #False
print(3 in t)
print(4 in l)
print('t' not in s)#True


#Operators for Sets and Dictionaries 
#Sets and frozensets支持下列操作
s1={3,4,5,6}
s2={4,5,7,8}
print(type(s1))
#key in s containment check 
print(3 in s1)
#key not in s non-containment check 
print(3 not in s1)
#s1 == s2 s1 is equivalent to s2 
print(s1==s2)
#s1 != s2 s1 is not equivalent to s2 
print(s1!=s2)
#s1 <= s2 s1 is subset of s2 
print(s1<=s2)
#s1 < s2 s1 is proper subset of s2 
print(s1<s2)
#s1 >= s2 s1 is superset of s2 
#s1 > s2 s1 is proper superset of s2 
#s1 | s2 the union of s1 and s2 
print(s1|s2)#{3, 4, 5, 6, 7, 8}
#s1 & s2 the intersection of s1 and s2 
print(s1&s2) #{4, 5}
#s1 − s2 the set of elements in s1 but not s2 
print(s1-s2)#{3, 6}
#s1 ˆ s2 the set of elements in precisely one of s1 or s2 
print(s1^s2) #{3, 6, 7, 8}
#Dictionaries支持下列操作
d1={'1':1,'2':2,'3':3}
d2={'2':2,'3':3,'4':4}
#d[key] value associated with given key 
print(d1['1'])
#d[key] = value set (or reset) the value associated with given key 
d1['1']=10
print(d1['1'])
#del d[key] remove key and its associated value from dictionary 
del d1['1']
print(d1['1']) #KeyError: '1'
#key in d containment check 
print('1' in d1) #False
#key not in d non-containment check 
print('1' not in d1)
#d1 == d2 d1 is equivalent to d2 
print(d1==d2)
#d1 != d2 d1 is not equivalent to d2
print(d1!=d2)








