#!/usr/bin/env python
# coding: utf-8

# In[72]:


#John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
#Given an array of integers representing the color of each sock,
#determine how many pairs of socks with matching colors there are.

def sockMerchant(n, ar):
    n = len(ar)
    dic = {i:ar.count(i) for i in ar}
    pair = []
    pair_count = []
    for i,j in dic.items():
        count = j//2
        pair.append({i:count})
        pair_count.append(count)
        
    print('This is the dictinary:',dic)
    print("------------------------------------------------------------")
    print('This is are the pairs:',pair)
    print("------------------------------------------------------------")
    print('This is are the pair_count:',pair_count)
    return sum(pair_count)


# Examples
#ar = [1,2,1,2,1,3,2]
ar = [9,10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(len(ar),ar)

