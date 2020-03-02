#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def divisibleSumPairs(n, k, ar):
    store = []
    for i in range(n):
        for j in range(n):
            if (ar[i] + ar[j]) % k == 0 and (i < j):
                store.append([ar[i], ar[j]])
    print(store)
    return len(store)

# Example
ar = np.array([1,2,3,4,5,6])
n = len(ar)
divisibleSumPairs(n,5,ar)


# In[ ]:




