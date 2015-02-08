# -*- coding: utf-8 -*-

"""
描述算法的运行时间、数据结构操作、和算法的空间使用

"""
from time import time

def test():
    start_time=time()
    #run
    end_time=time()
    elapsed=end_time-start_time
    print(elapsed)
    

if __name__ == '__main__':
    test()