#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
import numpy as np

def mulSpecial(arr):
    lisst = []
    for j in range(len(arr)):
        arr2 = np.delete(arr, j)   # deleting out the index of a specific element
        result = np.prod(arr2)
        lisst.append(result)
    return lisst

# Example
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([3,2,1])
print(mulSpecial(arr1))
print("---------------------------------")
print(mulSpecial(arr2))

