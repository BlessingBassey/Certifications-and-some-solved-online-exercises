#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np
# def countApplesAndOranges(s, t, a, b, apples, oranges):
# #     house_start_point = s
# #     house_end_point = t
# #     location_apple = a
# #     location_orange = b
# #     distance_apple = apples
# #     distance_orange = oranges
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = []
    count_orange = []
    num_apple = 0
    num_orange = 0
    
    for i in range(len(apples)):
        count1 = apples[i] + a
        count_apple.append(count1)
        
        if (count_apple[i] >= s) and  (count_apple[i] <= t):
            num_apple += 1
        
    for k in range(len(oranges)):
        count2 = oranges[k] + b
        count_orange.append(count2)
        
        if (count_orange[k] >= s) and (count_orange[k] <= t):
            num_orange += 1
     
        
    print(num_apple)
    print(num_orange)
    
countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])

