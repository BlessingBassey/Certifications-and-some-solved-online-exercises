#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Comapring each element in 2 list, which ever is bigger receives a point, if they are equal, no point for any one
# i.e  comparing triplet
import numpy as np
def compareTriplets(a, b):
    Alice =0
    Bob = 0

    for i in range(len(b)):        
        if a[i] > b[i]:
            Alice+=1
        elif a[i] == b[i]:
            print('Nobody receives a point')
        elif a[i] < b[i]:
            Bob+=1
    return [Alice,Bob]

#Example
a = np.array([1,2,3])
b = np.array([3,4,2])

compareTriplets(a, b)

