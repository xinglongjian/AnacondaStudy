# -*- coding: utf-8 -*-
"""
成员变量以下划线开头，比如_account，是private变量，其他类不能访问
以_开头的方法是protect
以__开头的方法是private

"""
class CreditCard: 
    """A consumer credit card.""" 
    def __init__ (self, customer, bank, acnt, limit): 
        """Create a new credit card instance. 
        The initial balance is zero.
        customer the name of the customer (e.g., John Bowman ) 
        bank the name of the bank (e.g., California Savings ) 
        acnt the acount identiﬁer (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars) 
        """
        self._customer = customer 
        self._bank = bank 
        self._account = acnt 
        self._limit = limit 
        self._balance = 0 
        
    def get_customer(self):
        """Return name of the customer.""" 
        return self._customer 
            
    def get_bank(self): 
        """Return the bank s name.""" 
        return self._bank
    def get_account(self):
        """Return the card identifying number (typically stored as a string).""" 
        return self._account 
    def get_limit(self):
        """Return current credit limit.""" 
        return self._limit 
    def get_balance(self): 
        """Return current balance.""" 
        return self._balance
    def charge(self, price): 
        """Charge given price to the card, assuming suﬃcient credit limit. 
        Return True if charge was processed; False if charge was denied. 
        """ 
        if price + self._balance > self._limit: # if charge would exceed limit, 
            return False # cannot accept charge 
        else: 
            self._balance += price 
            return True 
    def make_payment(self, amount): 
        """Process customer payment that reduces balance."""
        self._balance -= amount
        
    def __add__(self,other):
        """
        重载+操作符,又从新构造一个新的CreditCard实例
        """
        return self.__class__(self._customer,self._bank,self._account,self._limit+other._limit)
    
    def __str__(self):
        """
        重载str
        """
        return str(self._account+";"+self._bank)
        
if __name__=='__main__':
    card=CreditCard('John Bowman','California Savings','56 5391 0375 9387 5309', 2500)
    card1=CreditCard('John Bowman','California Savings','56 5391 0375 9387 5309', 3500)
    account=card.get_account()
    #测试两个对象相加    
    print((card+card1).get_limit())
    print(account)
    print(str(card1))
        