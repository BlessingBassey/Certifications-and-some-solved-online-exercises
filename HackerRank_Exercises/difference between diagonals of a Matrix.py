#!/usr/bin/env python
# coding: utf-8

# In[52]:


def diagonalDifference(arr):
    # Write your code here

    n = len(arr)
    left = 0
    right = 0
    for i in range(n):
        left += arr[i][i]
        right += arr[i][n - i - 1]
        #print(left)
        #print(right)

    return abs(left-right)

