#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:52:21 2020

@author: Dv
"""

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    
    
    if x<= y:
       return x*y
    else:
       return x/y
    raise NotImplementedError


def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    
    #x = np.vectorize(x)
    vfunc = np.vectorize(scalar_function)
    
    return vfunc(x,y)
    raise NotImplementedError
