# -*- coding: utf-8 -*-

"""
计算前n个值的平均数，并组成一个新的list
该函数的执行时间为O（n2）
"""

def prefix_average1(S):
    
    #该语句执行时间为常量时间 a
    n=len(S)
    
    """该语句是创建一个长度为n的list，并初始化每个元素为0，
    该操作和元素长度有关系,因此，执行时间为O（n）
    """
    A=[0]*n
    """外层循环会执行n次，而在循环内部的total=0和A[j]=total/(j+1)也会执行n次，
    因此再加上对j的控制，外层循环执行时间为O（n）
    """
    for j in range(n):
        total=0
        """
        内层循环的执行次数取决于j的值，因此内层循环的执行次数为1+2+3+...+n=n(n+1)/2=O(n2)
        """
        for i in range(j+1):
            total+=S[i]
        A[j]=total/(j+1)
    return A


"""
上面函数的另一种实现。

"""

def prefix_average2(S):
    n=len(S)
    A=[0]*n
    for j in range(n):
        """
        这里用一行语句代替类一个for循环，不过由于S[0:j+1]是构造一个新的list，因此他的执行时间也是O（j+1），
        而sum（S[0:j+1]）的执行时间也是O（j+1），所以该语句的执行时间为1+2+3+...+n=n(n+1)/2=O(n2)
        """
        A[j]=sum(S[0:j+1])/(j+1)
    return A
    

"""
第三个函数，是另一种实现。
在循环体内，每循环一次都累计之前的和，并计算出这一步的平均值存储到A中。
因此该函数的执行时间为O（n）
"""

def prefix_average3(S):
    
    n=len(S)
    A=[0]*n
    total=0
    for j in range(n):
        total+=j
        A[j]=total/j
    return A