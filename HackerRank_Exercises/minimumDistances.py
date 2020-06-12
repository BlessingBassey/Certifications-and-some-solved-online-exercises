#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
We define the distance between two array values as the number of indices
between the two values. Given , find the minimum distance between any pair 
of equal elements in the array. If no such value exists, print -1
'''

from collections import defaultdict
def minimumDistances_1(a):
    dic = defaultdict(list)     # create a default dictionary to have each value as the key and the index of that sam value in a list(print below to see well)
    list_min = []
    
    for idx,val in enumerate(a):
        dic[val] += [idx]
    print(dic)
    print("\n")
        
    for key in dic:
        if len(dic[key]) > 1:   # since we are concerned with indexes with double values, then we take keys having list of more than 1 element
            indices = dic[key]  # e.g key 3, hase 2 values as seen below
            distance = abs(indices[0] - indices[1])  # find the difference between this two values (use abs() to make it positive)
            list_min.append(distance)      # append into the empty list created above
            

    if len(list_min) > 0:                 #only print the minimum value from that list
        return min(list_min)
    return -1                             # if all the above condition is not met, print -1

# Note that the above efficiency is O(n)
# we can also have O(n^2) bellow ( although not efficient)


def minimumDistances_2(a):
    start = 0
    list_ = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] == a[j]:
                distance = abs(i - j)
                list_.append(distance)
    
    if len(list_) > 0:
        return min(list_)
              
    return -1

#Example
print("First method:",minimumDistances_1([3,2,1,2,3]))

print("-----------------------Below is efficiency of O(n^2)---------------------------")

print("Second method:", minimumDistances_2([3,2,1,2,3]))

