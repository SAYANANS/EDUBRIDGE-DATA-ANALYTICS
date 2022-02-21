#!/usr/bin/env python
# coding: utf-8

# ## calculate square of all numbers between 0-10 using list comprehensions

# In[5]:


n=list[0,1,2,3,4,5,6,7,8,8,10]
for i in range(0,10+1):
    print(i**2)


# ## Multiply whole list by 10

# In[7]:


n=list[0,1,2,3,4,5,6,7,8,8,10]
for i in range(0,10+1):
    print(i*10)


# ## Extract numbers from a string using list comprehension

# In[13]:


string="My age is 21 and my sisters age is 14"
s=[int(s) for s in str.split(string) if s.isdigit()]
print(s)


# ## Write a program to remove the duplicate element of the list

# In[14]:


duplicate=[2,4,10,20,5,2,20,4]
print(list(set(duplicate)))


# ## Write a program to find the sum of the element in the list

# In[21]:


l=[2,3,4,5,6,7,10]
sum=0
for i in range(0,len(l)):
    sum=sum+l[i]
print(sum)


# ## program to find the lists consist of at least one common element

# In[35]:


listA = [['Mon', 3, 'Tue', 7,'Wed',4],['Thu', 5,'Fri',11,'Tue', 7],['Wed', 9, 'Tue', 7,'Wed',6]]
print("Given list of lists : \n",listA)
res = list(set.intersection(*map(set, listA)))
print("The common elements among inners lists : ",res)


# In[ ]:




