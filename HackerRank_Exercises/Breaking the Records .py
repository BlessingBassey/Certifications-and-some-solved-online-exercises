#!/usr/bin/env python
# coding: utf-8

# In[10]:


def breakingRecords(scores):
    n = len(scores) 
    count_highest = 0
    count_lowest = 0
        
    higest_score = scores[0]
    lowest_score = scores[0]
    
    for score in range(n):
        if scores[score] > higest_score:
            higest_score = scores[score]
            count_highest += 1
                    
        if scores[score] < lowest_score:
            lowest_score = scores[score]
            count_lowest += 1
                    
    print (count_highest,count_lowest)
                    

# Example
import numpy as np
#b = np.array([10, 5 ,20, 20, 4, 5, 2, 25, 1])
b = np.array([3, 4 ,21, 36, 10, 28, 35, 5, 24, 42])

breakingRecords(b)


# In[ ]:




