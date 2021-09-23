# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:48:15 2021

@author: Amund
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return "".join([letter if letter in lettersGuessed else " _ " for letter in secretWord])
print(getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']))