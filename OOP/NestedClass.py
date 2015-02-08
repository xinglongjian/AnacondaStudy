# -*- coding: utf-8 -*-

class OuterClass:

    _name='outName'    
    
    def __init__(self,name):
        self._name=name
    
    def get_name(self):
        return self._name
        
    """
    定义一个内部嵌套类
    """    
    class InnerClass:
        
        def get_name(self,outer):
            #必须在外部类中声明该属性
            return outer._name

if __name__=='__main__':
    c=OuterClass("nestedclass")
    i=OuterClass.InnerClass()
    print(i.get_name(c))
    
    
    