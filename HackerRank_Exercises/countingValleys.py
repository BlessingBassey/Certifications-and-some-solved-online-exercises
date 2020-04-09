#!/usr/bin/env python
# coding: utf-8

# In[11]:


"""
Gary is an avid hiker. He tracks his hikes meticulously, 
paying close attention to small details like topography. 
During his last hike he took exactly $n$ steps. For every step he took, 
he noted if it was an uphill,$U$ , or a downhill, $D$ step. 
Gary's hikes start and end at sea level and each step up or down 
represents a $1$ unit change in altitude. We define the following terms:

(1)A mountain is a sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step down to sea level.
(2)A valley is a sequence of consecutive steps below sea level, 
starting with a step down from sea level and ending with a step up to sea level.

"""

def countingValleys(n, s):
    dic_steps = {'U':0, 'D':0}
    num_valleys = 0
    for step in s:
        dic_steps[step] += 1
        if step == 'U' and dic_steps['U'] == dic_steps['D']:
            num_valleys += 1
    return num_valleys

a = ['U','D','D','D','U','D','U','U']
b = ['D','D','U','U','D','D','U','D','U','U','U','D']
print('This is for step a :',countingValleys(len(a),a))
print('This is for step b :',countingValleys(len(b),b))


# In[ ]:




