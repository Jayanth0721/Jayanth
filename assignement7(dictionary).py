#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1 :-
mydict={"stuname":"Jayanth","stuage":"18","stucity":"bangalore"}
print("student age is:",mydict["stuname"])
print("student city is:",mydict["stucity"])


# In[3]:


#2 :-
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers+=x
    return sum_numbers
print(sum_list([4,-20,3]))


# In[6]:


#3 :-
n=4
l=[{} for __ in range(n)]
print(l)


# In[7]:


#4 :-
num={"physics":82,"math":75,"chemistry":88}
print(list(num)[1])


# In[12]:


#5 :-
d={"blue":3, "green":4, "Blue":2}
for color_key,value in d.items():
    print(color_key,"correspond to",d[color_key])


# In[14]:


#6 :-
my_dict={"n1":10,"n2":-54,"n3":50}
print(sum(my_dict.values()))


# In[17]:


#7 :-
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={}
for d in (dict1,dict2,dict3): dict4.update(d)
print(dict4)


# In[18]:


#8 :-
x={}
print(x)


# In[20]:


#9 :-
tuplex=("tuple",True,4.2,1)
print(tuplex)


# In[22]:


#10 :-
tup=("j","a","y","a","n","t","h")
str=" ".join(tup)
print(str)


# In[24]:


#11
tuplex=("j","a","y","a","n","t","h")
_slice=tuplex[2:]
print(_slice)


# In[25]:


#12 :-
tuplex=tuple("python")
print(tuplex)
print(len(tuplex))


# In[29]:


#13 :-
tuplex = ((1,'j'),(7,'h'))
print(dict((y,x) for x,y in tuplex))


# In[32]:


#14 :-
x=(5,10,15,20)
y=reversed(x)
print(tuple(x))


# In[35]:


#15 :-
l=[('j',1),('a',2),("y",3),('a',4),('n',5),("t",6),('h',7)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)    


# In[36]:


#16 :-
listx=[5,10,7,4,15,3]
tuplex=tuple(listx)
print(tuplex)


# In[ ]:




