#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Given an array of integers, find the sum of its elements.
import os
import sys

def simpleArraySum(ar):
    summ = 0
    for i in range(len(ar)):
        summ += ar[i]
    return summ 

#Example
simpleArraySum([1,2,3,4,5])

