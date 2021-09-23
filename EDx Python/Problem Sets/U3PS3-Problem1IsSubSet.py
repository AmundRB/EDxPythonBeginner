# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:58:44 2021

@author: Amund
"""
s = ["a"]
g = ["a"]
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    print(set(secretWord))
    print(set(lettersGuessed))
    return set(secretWord).issubset(lettersGuessed)
print(isWordGuessed("apple", ["a", 'l', 'p', 'e', 's', "z"]))