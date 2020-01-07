#!/usr/bin/env python
# coding: utf-8

# In[98]:


import numpy as np
def timeConversion(s):
    hh,mm,ss = s.split(':')
    hh = s.split(':')[0]
    #ss[-2] = AM or PM
    
    if hh == '12' and ss[-2:] == 'AM':
        hh = '00'
    if hh!= '12' and ss[-2:] == 'PM':
        hh = str(int(hh) + 12)
        
    return hh + ':' + mm + ':'+ ss[:-2]
    
# Example
b = '12:45:54PM'
timeConversion(b)


# In[ ]:




