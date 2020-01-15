#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

    The first kangaroo starts at location x1 and moves at a rate v1 of meters per jump.
    The first kangaroo starts at location x2 and moves at a rate v2 of meters per jump.
    
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.'''

def kangaroo_3(x1, v1, x2, v2):
    
    # x1 + n*v1 = x2 + n*v2, it implies that n = (x2 - x1) / (v1 - v2) 
    
    num = x2 - x1
    dem = v1 - v2
    if dem == 0 or (num%dem != 0 or num/dem < 0):
        return 'NO'            
    return 'YES' 


# Arithmetric progression method
def kangaroo_2(x1, v1, x2, v2):
    def get_value(a,n,d):
        return a + (n - 1)*d
    
    if x1 > x2:                      # What if the numbers are interchanged?
        x1, v1, x2, v2 = x2, v2, x1, v1    
    n = 1
    if v2 > v1:
        return ('NO')
    
        
    while True:
        k1,k2 = get_value(x1,n,v1) , get_value(x2,n,v2)   # This is the formular for Arithmetic Progression
                
        if k1 == k2:
            return 'YES'
        if k1 > k2:
                return 'NO'
        n += 1



# In[6]:


print(kangaroo_1(0, 3 ,4 ,2)) 

print(kangaroo_1(4, 2 ,0,3))  # Intercahnging the numbers above
 
print(kangaroo_1(0,2,5,3))


# In[7]:


print(kangaroo_2(0, 3 ,4 ,2)) 

print(kangaroo_2(4, 2 ,0,3))  # Intercahnging the numbers above
 
print(kangaroo_2(0,2,5,3))

