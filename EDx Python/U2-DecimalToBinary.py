# -*- coding: utf-8 -*-
"""
Created on 08.09.21

@author: Amund
"""
num = 19
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num%2) + result
    print(result + " T " + str(num))
    num = num//2
if isNeg:
    result = "-" + result
    