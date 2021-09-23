# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:04:58 2021

@author: Amund
"""
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alp = string.ascii_lowercase
    available = ""
    for letter in alp:
        if letter not in lettersGuessed:
            available += letter
    return available
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
            
        

        