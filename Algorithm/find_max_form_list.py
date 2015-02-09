# -*- coding: utf-8 -*-

"""
该算法为从list中查找最大的数。
如该判断修改maxdata的次数，可以分几种情况：
1、最坏的：list中顺序按照从小到大排列，那么，所有数字都比较完后才能得到最大值，
   所需时间跟元素个数有关系，因此时间复杂度为O（n）
2、最好的：list中顺序按照从大到小排列，那么，第一个数字就是最大值，O（1）
3、平均的：list中顺序随机排列，那么时间复杂度为O（logn）


对该算法进行时间复杂度分析，
"""
from time import time

def find_max(data):
    maxdata=data[0]  #赋值操作，固定时间a
    for i in data:   #循环执行n次
        if i>maxdata: #比较操作，固定时间b
            maxdata=i #赋值操作，固定时间a
    return maxdata   #返回操作，固定时间c


if __name__ =='__main__':
    
    d1=[1,2,3,4,5,6,7,8,9,10]
    d2=[3,2,4,5,1,9,10,8,7,6]
    
    start_time=time()
    find_max(d1)
    end_time=time()
    print("Worst:"+str(end_time-start_time))
    
    start_time=time()
    find_max(d2)
    end_time=time()
    print("Average:"+str(end_time-start_time))
    
