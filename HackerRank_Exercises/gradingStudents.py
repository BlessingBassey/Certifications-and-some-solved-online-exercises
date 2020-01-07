#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
def gradingStudents(grades):
    for i in range(len(grades)):
            

        if grades[i] < 38:
            grades[i] = grades[i]

        if grades[i] >= 38:
            round_up_1 = grades[i] + 1
            round_up_2 = grades[i] + 2


        if grades[i] >= 38 and (round_up_1)%5 == 0:
            grades[i] = round_up_1

        if grades[i] >= 38 and (round_up_2)%5 == 0:
            grades[i] = round_up_2

        if grades[i] >= 38 and (round_up_1)%5 != 0:
            grades[i] = grades[i]
            
        if grades[i] >= 38 and (round_up_2)%5 != 0:
            grades[i] = grades[i]
        
    return grades

# example
gradingStudents([73,67,38,33])


# In[ ]:




