#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price, "p" dollars.
However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. 
Specifically, the first game you buy during the sale will be
sold at "p"  dollars, but every subsequent game you buy will be sold at 
exactly "d"  dollars less than the cost of the previous one you bought. This will continue until the cost becomes less than or equal to "m" dollars,
after which every game you buy will cost  dollars each.
'''
def howManyGames_1(p, d, m, s):
    if s<p:
        return 0
    list_ = [p]
    while p > m and p-m >= d:
        p -= d
        list_.append(p)
    sum_list = sum(list_)
    if s >= sum_list:
        rem = (s-sum_list)//m
        return len(list_)+rem
    # now lets attend to the case were s < sum_list
    sum_list = 0
    for i, v in enumerate(list_):
        sum_list += v
        if sum_list > s:
            return i
    return len(list_)

   
def howManyGames_2(p, d, m, s):
    count = 0
    while s >= m and s >= p:
        s -= p
        p -= d
        if p <= m:
            p = m
        count += 1
    return count
    
    
# Example
print(howManyGames_1(100, 19, 1, 180))
print(howManyGames_2(100, 19, 1, 180))
print("\n")
print(howManyGames_1(20, 3, 6, 85))
print(howManyGames_2(20, 3, 6, 85))


# In[ ]:




