# -*- coding: utf-8 -*-
"""
Created on 08.09.21

@author: Amund
"""
s = "aeio u"
NumVowels = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(char)
        NumVowels += 1

print("Number of vowels: " + str(NumVowels))
        
    