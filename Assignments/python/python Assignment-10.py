#!/usr/bin/env python
# coding: utf-8

# ## Write a function to find the Max of three numbers.

# In[3]:


def maximum(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)
        
num1=int(input("Enter the first number")) 
num2=int(input("Enter the second number")) 
num3=int(input("Enter the third number")) 
maximum(num1,num2,num3)

    


# ## Write a function to sum all the numbers in a list

# In[39]:


def sum1(list):
    return sum(list)
list=[6,7,8]
sum1(list)
    


# ## Write a function to multiply all the numbers in a list

# In[37]:


def mul(list):
    result=1
    for i in list:
        result=result*i
    print(result)

list=[2,3,4]
mul(list)
        
        
        


# ## Write a function to reverse a string

# In[16]:


def rev(s):
    print(s[: :-1])
string=input("Enter a string\n") 
rev(string)


# ## Write a function to calculate the factorial of a number

# In[20]:


def fact(num):
    f=1
    i=1
    while i<=num:
        f=f*i
        i=i+1
    return f
num=int(input("enter the number\n"))
result=fact(num)
print("The factorial of this number is ",result)


# ## Write a function that accepts a string and calculate the number of upper case letters and lower case letters 

# In[26]:


def stri(s):
    lower,upper=0,0
    for i in s:
        if(i.islower()):
            lower=lower+1
        elif(i.isupper()):
            upper=upper+1
    print(lower)
    print(upper)
si=input("enter the string")
stri(si)


# ## Write a function that takes a list and returns a new list with unique elements of the first list

# In[33]:


def unique(list):
    unique_list=[]
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list) 
    
list=[10,10,20,40,50,50,60]
print("The unique values of the list is")
unique(list)

            


# In[ ]:




