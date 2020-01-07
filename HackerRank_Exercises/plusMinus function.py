#!/usr/bin/env python
# coding: utf-8

# In[54]:


import math 

def plusMinus(arr):
    positive_num = []
    negavtive_num = []
    zeros = []
    
    for i in (arr):
        if i > 0:
            positive_num.append(i)
        if i < 0:
            negavtive_num.append(i)
        if i == 0:
            zeros.append(i)
    a = len(positive_num)/len(arr)
    b = len(negavtive_num)/len(arr)
    c = len(zeros)/len(arr)
            
    #return positive_num,negavtive_num,zeros
    #print round((a,6),(b,6),(c,6))
    
    print (end="") 
    print ("{0:.6f}".format(a)) 
    
    print (end="") 
    print ("{0:.6f}".format(b))
    
    print (end="") 
    print ("{0:.6f}".format(c))

    
# Example
a = np.array([-4, 3, -9 ,0, 4, 1])
plusMinus(a)

