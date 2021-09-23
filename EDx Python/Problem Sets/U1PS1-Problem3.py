# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:08:07 2021

@author: Amund
"""

s = 'azcbobobegghakl'
Tempstore = ""
store = ""
for i in range(len(s)):
    if Tempstore == "" or s[i] >= Tempstore[-1]:
        Tempstore += s[i]
        print(Tempstore + str(i))
    elif Tempstore[-1] > s[i]:
        if store == "" or len(Tempstore) > len(store):
            store = Tempstore
            Tempstore = s[i]
            print("Elif store: " + store)
if len(Tempstore) > len(store):
    store = Tempstore
print(store)
