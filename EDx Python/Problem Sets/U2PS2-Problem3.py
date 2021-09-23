# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:21:21 2021

@author: Amund
"""

balance = 320000
annualInterestRate = 0.2
def debt(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    minimum = balance/12
    maximum = (balance *(1 + monthlyInterestRate)**12)/12
    epsilon = 0.01
    inbal = balance
    guess = (minimum + maximum)/2
    while inbal >= epsilon:
        guess = (minimum + maximum)/2
        
        for i in range(1,13):
            newBalance = inbal - guess
            monthlyInterestRate = annualInterestRate/12*newBalance
            inbal = newBalance+monthlyInterestRate
        if inbal < 0:
            maximum = guess
            inbal = balance
        elif inbal > epsilon:
            minimum = guess
            inbal = balance
        else:
            return guess

print("Lowest Payment: " + str(round(debt(320000, 0.2), 2)))