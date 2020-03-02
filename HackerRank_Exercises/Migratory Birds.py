#!/usr/bin/env python
# coding: utf-8

# In[84]:


import numpy as np

def migratoryBirds(arr):
    dic = {}                # get the elements and their respective counts ina dictionary
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1
    
    initial_k, initial_v = arr[0], dic[arr[0]]      # randomly pick any initialization
    for k,v in dic.items():
        if (v > initial_v) or (v == initial_v and k < initial_k):   # note all the conditions
            initial_k, initial_v = k, v
            
    print('The dictionary' ,dic)
    print("--------------------------------------------------------------------------------------------")
    print(dic.items())
    print("----------------------------------------------------------------------------------------------")
    print('The smallet key with the maximum elemet is:', initial_k)      
    
    
# Example
arr = np.array([5 ,11, 1, 2,9,9,9, 3, 4, 8, 4, 3, 2, 1, 3, 4])
migratoryBirds(arr)


# In[ ]:




