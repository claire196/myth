#!/usr/bin/env python
# coding: utf-8

# In[52]:


def Bal(str1):
    a = str1
    l = 0
    r = 0
    while len(a) > 0:
        if a[0] == 'r':
            r = r+1
        elif a[0] == 'l': 
            l = l+1
        else:
            return -1
        a = a[1:]
    if r == l:
        return 1
    else: return 0
    
def BalM(str1):
    if Bal(str1) == -1 or Bal(str1) == 0:
        print('Error: string is disbalanced')
        return -1 
    n = 1
    cnt = 0
    i = 0
    while i < len(str1):
        if Bal(str1[i:i+2]) == 1:
            cnt = cnt + 1
            i = i + 2
        else: 
            i = i + 1
    return cnt   
                


# In[54]:


BalM('llrllrrr')


# In[51]:


def BalMW(str1):
    if Bal(str1) == -1 or Bal(str1) == 0:
        print('Error: string is disbalanced')
        return -1 
    n = 1
    cnt = 0
    for i in range(len(str1)):
        if Bal(str1[i:i+2]) == 1:
            cnt = cnt + 1
            i = i + 2
            print('cnt=',cnt)
            print(i)
        else: 
            i = i + 1
            print('cnt=',cnt)
            print(i)
    return cnt   
                
            
    
    


# In[ ]:





# In[4]:


Bal('lr')


# In[48]:




