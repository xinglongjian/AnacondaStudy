# -*- coding: utf-8 -*-
"""
定义抽象类
"""
from abc import  ABCMeta, abstractmethod 

class Sequence(metaclass=ABCMeta): 
    
    
    @abstractmethod 
    def len (self): 
        """定义一个抽象方法
        Return the length of the sequence.
        """

"""
继承抽象类，实现抽象方法
"""
class SequenceImpl(Sequence):
    
    def len(self):
        return  10



if __name__ =='__main__':
    si=SequenceImpl()
    print(si.len())