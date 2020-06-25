#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 area of circle using math module

import math
r=float(input("enter radius of circle "))
a=math.pi*(r**2)
print("area of circle=",a)


# In[2]:


#2 area of regular polygon using math module
import math
n=int(input("enter no of sides "))
l=float(input("enter a length of a polygon"))
a=(n*1**2)/(4*math.tan(math.pi/n))
print("area of regular polygon=",a)


# In[4]:


#3 area of segment of circle
import math
t=float(input("enter the angle to measure"))
r=float(input("enter radius of circle"))
if t>=360:
          print("the angle is not possible")
else:
    a=(math.pi*(r**2)*(t/360))-((1/2)*(r**2)*math.sin((t*math.pi)/180))
    print("the area of segment is ",a)


# In[5]:


#4 generating a random no from list
import random
print("random no from list is")
print(random.choice([100,1,2,3,50,40]))


# In[6]:


#5 gnerating random no b/w 1-10000 with difference 50
import random
print("the random nos b/w 1-10000",random.randrange(1,10000,50))


# In[10]:


#6 calculating using math module
import math
print("value of sin(60)is",math.sin(60))
print("value os cos(pi)is",math.cos(math.pi))
print("value oftan(90)is",math.tan(90))
print("angle of sin(0.8660254037844386)is",math.degrees(math.asin(0.8660254037844386)))
print("value of 5^8 is",5**8)
print("value of squareroot of 400 is",math.sqrt(400))
print("value of 5^e is",5**math.e)
print("value of log(1024) base 2 is",math.log(1024,(2)))
print("floor value of 23.56 is",math.floor(23.56))
print("ceiling value of 23.56 is",math.ceil(23.56))

