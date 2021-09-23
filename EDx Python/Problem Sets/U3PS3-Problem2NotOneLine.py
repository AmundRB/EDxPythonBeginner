# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:31:11 2021

@author: Amund
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    current = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            current += letter
        else:
            current += " _ "
    return current
    return = "".join(letter) if letter in lettersGuessed
print(getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']))