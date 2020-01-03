#!/usr/bin/env python
# coding: utf-8

# In[273]:


def miniMaxSum1(arr):
    sorting = sorted(arr)
    min_list = sorting[0:-1]

    max_list = sorting[1:]

    minni = 0
    maxxi = 0
    

    for i in (min_list):
        minni += i
    
    for j in (max_list):
        maxxi += j
    final = minni,maxxi
    print(minni,maxxi)
    
#This code above can be optimize as follows, for better computational complexity.
    
    
def miniMaxSum2(arr):
    min=10**10
    max = -1
    idx_min=-1
    idx_max=-1
    
    for i, x in enumerate(arr):
        if min>x:
            min=x
            idx_min=i
        if max<x:
            max=x
            idx_max=i
    
    minni = sum([arr[i] for i in range(len(arr))  if i!= idx_max])
    maxxi = sum([arr[i] for i in range(len(arr))  if i!= idx_min])

    print(minni,maxxi) 


b = [random.randint(1,100) for i in range(10**7)]
        
miniMaxSum1(b)    
miniMaxSum2(b)


# In[274]:


import time


# In[275]:


start = time.time()
miniMaxSum1(arr)
end = time.time()
print(end-start)


# In[276]:


start = time.time()
miniMaxSum2(arr)
end = time.time()
print(end-start)


# In[ ]:




