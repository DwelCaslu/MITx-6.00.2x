# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:10:09 2017

@author: .LUCAS
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    else: 
        #Calculating the mean length of the strings in the list
        summ_length = 0
        for i in range(len(L)):
            summ_length += len(L[i])
        

        mean_length = summ_length/len(L)

        #Calculating the standard deviation:
        summ_diffs = 0 
        for i in range(len(L)):
            summ_diffs += (len(L[i]) - mean_length)**2
        std_dev = (summ_diffs/len(L))**(1/2)
        
        return std_dev

L = []
#L = ['a', 'z', 'p']
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))

