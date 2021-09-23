# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:40:35 2021

@author: Amund
"""

epsilon = 0.01
y = 54
guess = y/2
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    print("NumGuesses: " + str(numGuesses))
    guess = guess - (((guess**2) - y)/(2*guess))
    print("Guess: " + str(guess))
    print("Condition: "+ str(abs(guess*guess - y)))
print("NumGuesses Fin = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess))
'''
   x: int or float.
'''