# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:32:59 2021

@author: Amund
"""

s = "bobbboobobobobobbbob"
check = ""
count = 0
for char in s:
    if char == "b":
        check += char
        if check == "bob":
            count += 1
            check = "b"
        elif check == "bb":
            check = "b"
    elif char == "o" and check == "b":
        check += char
    else:
        check = ""

print("Number of times bob occurs is: " + str(count))