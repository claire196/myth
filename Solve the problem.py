#!/usr/bin/env python
# coding: utf-8

# In[1]:


def MFP (str1, str2):
    if len(str1) != len(str2):
        return 0
    else: 
        for i in range(len(str1)):
            if str1[i]==str2[(len(str2)-i-1)]:
                continue
            else: 
                return 0
                break
        return 1
    
    

    
            


# In[12]:


def MSP(a, b):
    str1 = a
    str2 = b
    if len(a) != len(b):
        return 0
    while len(str1) > 0:
        for j in range(len(b)):
            if str1[0] == str2[j]:
                str2 = str2[:j-1]+str2[j+1:]
                str1 = str1[1:]
                break
            elif len(str2)-1 == j:
                return 0
                break
        return 1
            
                            
                

