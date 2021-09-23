# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:22:26 2021

@author: Amund
"""
correct = True
low = 0
high = 100
print("Please think of a number between 0 and 100!")
while correct:
    guess = (low + high)//2
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while answer != "l" and answer != "h" and answer != "c":
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    elif answer == "c":
        print("Game over. Your secret number was: " + str(guess))
        correct = False