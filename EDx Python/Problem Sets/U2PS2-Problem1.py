# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:08:54 2021

@author: Amund
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12
def debt(annualInterestRate, monthlyPaymentRate, balance):
    monthlyInterestRate = annualInterestRate/12
    paid = 0
    months = 1
    while months < 13:
        paid += balance * monthlyPaymentRate
        balance = balance - (balance * monthlyPaymentRate)
        balance = balance + (balance * monthlyInterestRate)
        print("Month " + str(months) + " Remaining balance: " + str(round(balance, 2)))
        months += 1
    return round(balance, 2)
print("Remaining balance: " + str(debt(annualInterestRate, monthlyPaymentRate, balance)))