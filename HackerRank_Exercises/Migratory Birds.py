#!/usr/bin/env python
# coding: utf-8

# In[204]:


import numpy as np

def dayOfProgrammer(year):
    day_of_pro = 256
    leap_year = [31,29,31,30,31,30,31,31]
    
    if year == 1918:     # This is a special case, because of the trasition. 
        day_of_month = (day_of_pro - sum(leap_year)) + 1 + 13        
    
    if year in range (1700,1918):     #This is the Julian calender
        if year % 4 == 0:        
            day_of_month = day_of_pro - sum(leap_year)

        if year % 4 != 0 :
            day_of_month = (day_of_pro - sum(leap_year)) + 1
            
    if year in range (1919,2701):     # This is the Gregorian calender
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):        
            day_of_month = day_of_pro - sum(leap_year)

        else:
            day_of_month = (day_of_pro - sum(leap_year)) + 1

    return (str(day_of_month) + '.' +'0'+ str(len(leap_year)+1) + '.'+ str(year))
    

# Examples
print(dayOfProgrammer(1918))
print(dayOfProgrammer(2017))
print(dayOfProgrammer(2016))
print(dayOfProgrammer(1970))
print(dayOfProgrammer(2700))


# In[ ]:




