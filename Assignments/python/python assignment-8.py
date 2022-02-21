#!/usr/bin/env python
# coding: utf-8

# ## sort a dictionary by value

# In[1]:


markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist = sorted(markdict.items(), key=lambda x:x[1])
sortdict = dict(marklist)
print(sortdict)


# ## Add a key to the dictionary

# In[4]:


dict = {1:'geeks', 2:'fill_me'}
print("Current Dict is: ", dict)
dict[3] = 'geeks'
print("Updated Dict is: ", dict)


# In[ ]:




