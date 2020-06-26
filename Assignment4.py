#!/usr/bin/env python
# coding: utf-8

# In[6]:


#first and last digit
num=int(input('enter no'))
def a(num):
          while(num>=10):
                    num=num/10
                    return int(num)
def z(num):
          num=num%10
          return num
print("the first digit in no is",a(num),"the last digit is",z(num))


# In[10]:


#2 fibbonacci series
n=int(input("length 0f fibboncci series"))
a=0
b=1
count=0
if n<0:
    print("error")
elif n==1:
    print(a)
else:
    print("the fibbonacci series is")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1


# In[7]:


#3 marks of students
n=int(input("enter no of student "))
if n>=0:
    student=["member"]
    for i in range(0,n):
        name=input("enter name of student")
        print(name)
        mark=int(input("enter marks out of 100 "))
        print(mark)
        if(mark<40):
                student.append(name)
                print("this student is failed")
        else:
            print("you have passed")
    for i in range(1,len(student)):
         print(student[i])
else:
     print("invalid input")
    


# In[33]:


#4 multiplication table
n=int(input("which multiplication table do you want"))
for i in range(1,11):  
  print (n,"x",i,"=",n*i)


# In[34]:


#5 taking number
sum=0
c=0
num=int(input("enter no"))
while num!=-1:
    c+=1
    sum+=num
    num=int(input())
print(sum/c)   

