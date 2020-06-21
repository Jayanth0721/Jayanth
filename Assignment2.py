#!/usr/bin/env python
# coding: utf-8

# In[29]:


#1 eligible to vote
age=int(input("enter age  "))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible")


# In[32]:


#2 even or odd
n=int(input("enter a no"))
if(n%2==0):print('even no')
else:
         print('odd no')


# In[6]:


#3 string reversing
str="hello"
slicedstr=str[::-1]
print(slicedstr)


# In[51]:


#4 +ve number or not
n=int(input("enter a no"))
if(n>0):print("+ve no")
else:
     print("not +ve no")


# In[2]:


#5 quadratic equation

a=float(input("enter a no "))
b=float(input("enter a no "))
c=float(input("enter a no "))
d=(b*b)-(4*a*c)
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
if(d>0):
        print("roots are real and distinct")
if(d<0):        
        print("roots are imaginary")
if(d==0):
         print("roots are equal")


# In[68]:


#6 +ve/-ve/0 using nested if

a=int(input("enter a no "))
if a>0:
       print("no is +ve")
if a<0:
       print("no is -ve")
if a==0:
     print("zero") 


# In[10]:


#7 print given no

n=int(input("enter no 1 to 5 "))
number=('','one','two','three','four','five')
print(number[n])


# In[11]:


#8 vowels or consonant

ch=input("enter a char ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'): print("vowels")
else:
      print("consonant")

