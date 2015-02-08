# -*- coding: utf-8 -*-
"""
类的继承
"""
from CreditCard import CreditCard

class MyCreditCard(CreditCard):
    
    def __init__(self,customer, bank, acnt, limit):
        super().__init__(customer, bank, acnt, limit)
        


if __name__ == '__main__':
    c=MyCreditCard("customer","asdfaf","123 456 678",1000)
    print(c.get_limit())
        