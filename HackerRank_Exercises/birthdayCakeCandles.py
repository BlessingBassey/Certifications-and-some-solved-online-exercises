#!/usr/bin/env python
# coding: utf-8

# In[100]:


#import numpy as np
import numpy as np

def birthdayCakeCandles(ar):
    sorting = sorted(ar)
    max_candle = sorting[-1]
    max_candles = []
    
    for i in sorting:
        if i == max_candle:
            max_candles.append(i)
    return len(max_candles)

# This can be optizes as follows

def birthdayCakeCandles2(ar):
    max_candle = -1
    max_candles = 0
    for i in ar: 
        if i > max_candle:
            max_candle = i
            max_candles = 1
        elif i == max_candle:
            max_candles +=1
    return max_candles

# Example
c = np.array([2,3,6,1,4,6,1,5])
birthdayCakeCandles2(c)


# In[ ]:





# In[ ]:




