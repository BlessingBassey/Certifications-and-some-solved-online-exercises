#!/usr/bin/env python
# coding: utf-8

# In[41]:


def multiple(arr,n):       # I need a number 'n', such that every element in the array 'arr' is a factor of that number
    for i in arr:
        if n % i !=0:
            return False
    return True
        

def divisible(arr,n):  #I need a number 'n', such that 'n' is a factor of every element in the array 'arr'
    for i in arr:
        if i % n !=0:
            return False
    return True

def getTotalX(a, b): 
    count = 0
    n = min(a)
    while n <= max(b):
        if multiple(a,n) and divisible (b,n):
            count += 1
            print(n)
        n = n + min(a)
          
    return count


# In[42]:


import numpy as np
a = np.array([2,4])
b = np.array([16,32,96])


# In[43]:


getTotalX(a, b)


# In[ ]:




