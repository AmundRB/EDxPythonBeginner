# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:43:20 2021

@author: Amund
"""

balance = 3329
annualInterestRate = 0.2
def debt(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    inibal = balance
    LowPay = 10
    months = 1
    while months < 13:
        balance -= LowPay
        balance = balance + (balance * monthlyInterestRate)
        print("Month " + str(months) + " Remaining balance: " + str(round(balance, 2)))
        months += 1
        if balance <= 0 and months == 13:
            return LowPay
        elif balance >= 0 and months == 13:
            months = 1
            balance = inibal
            print("BALANCE AT START OF NEW LOOP: " + str(balance))
            LowPay += 10
            print("LOWEST PAYMENT AT START OF NEW LOOP: " + str(LowPay))
print("Lowest Payment: " + str(debt(3329, 0.2)))            
        
