#!/usr/bin/env python
# coding: utf-8

# In[369]:


##Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. 
##Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. 
##Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# bill: an array of integers representing the cost of each item ordered 
# k: is an integer representing the zero-based index of the item Anna doesn't eat
# b: is the amount of money that Anna contributed to the bill   

def bonAppetit(bill, k, b):  
    Ann_allegic = bill[k]                        # locating the item Anna doesn't want to eat      
    Anns_new_pay = (sum(bill) - Ann_allegic)//2  # Deductin the cost of Anna's allegic item from the initially money Anna contibuted
    if b == Anns_new_pay:                        # if the new_cost == the money that Anna initially contributed to the bill 
        return ('Bon Appetit')
    else:
        return (b - Anns_new_pay)                # deduct Anna's_new_pay from the initial contribution she made, this would be the amount 
                                                 # Brain would refund Anna
        
        
# Example
print(bonAppetit([3,10,2,9],1,12))
print()
print("--------------------------------------------------------------------------------------")
print(bonAppetit([2,4,6],2,3))


# In[368]:


# One might want to print their individual bills, bellow is the code for it

def bonAppetit(bill, k, b):  
    Ann_allegic = bill[k]
    brians_pay = sum(bill)//2
    Anns_pay = (sum(bill) - Ann_allegic)//2
    print("Brain's bill is:", bill)
    ann_bill = bill.pop(k)
    print("Anna's bill is:",bill)

    
    if b == Anns_pay:                        
        return ('Bon Appetit')
    else:
        return (b - Anns_pay)                
        
        
# Example
print(bonAppetit([3,10,2,9],1,12))
print()
print("--------------------------------------------------------------------------------------")
print(bonAppetit([2,4,6],2,3))

