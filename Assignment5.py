#!/usr/bin/env python
# coding: utf-8

# In[1]:


# length of string
str=input("enter string")
print("length of string",len(str))


# In[11]:


# character frequency
def char_frequency(str1):
    dict={ }
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_frequency('google.com'))


# In[10]:


# to get singlestring from two string
def chars_mix_up(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a+''+new_b
print(chars_mix_up("abc ","xyz"))


# In[13]:


#4 string display in upper and lower case

user_input=input("what is your fav lang?")
print("my fav lang is ",user_input.upper())
print("my fav lang is ",user_input.lower())


# In[14]:


# to remove a newline in python
str1="python excerise\n"
print(str1)
print(str1.rstrip())


# In[15]:


# to count occurrence of a substring
str1="the quick brown fox jumps over the lazy dog."
print()
print(str1.count("fox"))
print()


# In[22]:


# convert string in list
str1="apple,mango,banana"
print(f'list of items={str1.split(",")}')


# In[17]:


# to print character of a string using loop
x=input("enter a string")
for i in x:
    print(i)


# In[20]:


# to find the length without using len()
a='refrigerator'
count=0
for i in a:
    count=count+1
print(count)

