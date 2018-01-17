# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:12:20 2017

@author: .LUCAS
"""

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    count = 0
    for line in inFile:
        count+=1
        fields = line.split()
        #print(count)
        print(fields)
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)


print(loadFile())
#loadFile()