# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:17:15 2017

@author: .LUCAS
"""
import numpy as np
 
def search_comb(choices, total, n=None):
    """
    Assumes choices is a descending sorted list.
    Recursively searches for all combinations of choices such that their sum is equal to total.
    Returns closest from below if no exact match is found.
    """
 
    ## setup and base cases
     
    if total == 0 or n == 0:    return []   # degenerate cases
     
    ## trim too big elements
    i = 0
    while i < len(choices) and choices[i] > total: i += 1
    if i == len(choices):       return []   # all elements are greater than total
    _choices = choices[i:]
     
    if n and n > len(_choices): return []   # combination length exceeds available elements
 
    ## by now the first element is less or equal to total
    best_so_far = [_choices[0]]
    if best_so_far[0] == total: return best_so_far # we're lucky
     
    if n: # this is recursive call
        for i in range(len(_choices)-n+1):  # iterate through elements, exclude redundant calls
            c = _choices[i]
 
            if n == 1:  # just check each element, no recursion
                res = [c]
            else:       # recur
                res = [c] + search_comb(_choices[i+1:], total-c, n-1)
 
            if sum(res) == total: return res # exact match
            elif sum(res) > sum(best_so_far): best_so_far = res
 
    else: # main loop of breadth-first search
        for i in range(1, len(_choices)+1): # iterate through all possible combination lengths
            res = search_comb(_choices, total, i)
            if res:
                if   sum(res) == total: return res # exact match found
                elif sum(res) > sum(best_so_far): best_so_far = res
 
    return best_so_far # no exact match found
 
 
def find_combination(choices, total):
    """
    choices: a non-empty numpy.array of ints
    total: a positive int
  
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
 
    choices_list        = list(choices)
    choices_descending  = sorted(choices_list, reverse=True)
    combination         = search_comb(choices_descending, total)
 
    # build indexes list
    idx_list = []
    if combination:
        last_elem       = None
        last_elem_idx   = -1
        for elem in combination:
            if elem != last_elem:
                idx             = choices_list.index(elem)
                last_elem       = elem
                last_elem_idx   = idx
            else:
                idx             = choices_list.index(elem, last_elem_idx+1)
                last_elem_idx   = idx
            idx_list.append(idx)
 
    # build results list
    res = [0]*len(choices_list)
    for i in idx_list: res[i] = 1
     
    return np.asarray(res, dtype='int32')