#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:33:00 2020

@author: Dv
"""

import numpy as np
from matplotlib import pyplot as plt


X = np.array([
    [-1,-1],
    [1,0],
    [-1,10],
    # [-1,1],


])

y = np.array([1,-1,1])





X = np.array([
    # [-1,-1],
    [1,0],
    [-1,10],
    [-1,-1],


])

y = np.array([-1,1,1])

X = np.array([
    [-4,2],
    [-2,1],
    [-1,-1],
    [2,2],
    [1,-2],



])

y = np.array([1,1,-1,-1,-1])

X = X[::-5]
y = y[::-5]





# Xx = np.random.shuffle(X)

print('This is X')
print(X)
print('.......')
def perceptron_sgd(Xx, Y):
    w = np.zeros(2)
    eta = 1
    epochs = 2
    # print(w)
    # combination=[]
    miss=[]
    NotOK=0
    OK = 0 
    for t in range(epochs):

        for i, x in enumerate(X):
            # print('This is i')
            # print(i)
            # print('This is x')
            # print(x)
            if (np.dot(X[i], w)*Y[i]) <= 0:
                # print(np.dot(X[i+1], w)*Y[i+1])
                print('+++')
                # print('not ok')
                print(X[i])
                miss.append(X[i])
                w = w + eta*X[i]*Y[i]
                print('Nuevo W')
                print(w)
                NotOK= NotOK + 1
            else:
                print('OK')
                print(X[i])
                OK = OK+1
                
    print(NotOK)
    print(OK)
    # print(miss)
    return w,miss

w = perceptron_sgd(X,y)
print(w)



# This is X
# [[ 1 -2]
#  [-1 -1]
#  [ 2  2]
#  [-2  1]
#  [-4  2]]
# .......
# [ 1. -2.]
# 1
# [ 1. -2.]
#%%
for d, sample in enumerate(X):
    # Plot the negative samples
    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    # Plot the positive samples
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# Print a possible hyperplane, that is seperating the two classes.
plt.plot([-2,6],[6,0.5])


#%%

X = np.array([
    [-1,1],
    [-1,-1],
    [1,1],
    [2,2],


])

y = np.array([1,1,-1,-1])

# X = X[::-5]
# y = y[::-5]





# Xx = np.random.shuffle(X)

print('This is X')
print(X)
print('.......')
def perceptron_sgd(Xx, Y):
    w = np.zeros(2)
    eta = 1
    epochs = 4
    # print(w)
    # combination=[]
    miss=[]
    NotOK=0
    OK = 0 
    for t in range(epochs):

        for i, x in enumerate(X):
            # print('This is i')
            # print(i)
            # print('This is x')
            # print(x)
            if (np.dot(X[i], w)*Y[i]) <= 0:
                # print(np.dot(X[i+1], w)*Y[i+1])
                print('+++')
                # print('not ok')
                print(X[i])
                miss.append(X[i])
                w = w + eta*X[i]*Y[i]
                print('Nuevo W')
                print(w)
                NotOK= NotOK + 1
            else:
                print('OK')
                print(X[i])
                OK = OK+1
                
    print(NotOK)
    print(OK)
    # print(miss)
    return w,miss

w = perceptron_sgd(X,y)
print(w)