#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
She can jump on any cumulus cloud having a number that is equal to the number of the 
current cloud plus $1$ or $2$ . She must avoid the thunderheads.
Determine the minimum number of jumps it will take Emma to jump from her 
starting postion to the last cloud. It is always possible to win the game.

"""
def jumpingOnClouds(c):
    jump = 0
    count = 0
    
    while jump < len(c)-1:
        if jump+2 < len(c) and c[jump+2] == 0:
            jump+= 2
        else:
            jump+= 1
        count += 1
    return count

# Examples
c = [0,1,0,0,0,1,0]
d = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
print("c would have to jump {} times:".format(jumpingOnClouds(c))) 
print("---------------------------------------------------------------")
print("d would have to jump {} times:".format(jumpingOnClouds(d)))


# In[ ]:




