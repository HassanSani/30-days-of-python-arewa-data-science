#!/usr/bin/env python
# coding: utf-8

# In[2]:


# question 1-4

age=31
height=6.5
complex_number=2+4j
print(age)
print(height)
print(complex_number)


# In[5]:


#question 5.  Write a script that prompts the user to enter side a, side b, and side c of the triangle.
#Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
#Enter side b: 4
#Enter side c: 3
#The perimeter of the triangle
side_a = int(input('Enter side a:'))
side_b = int(input('Enter side b:'))
side_c = int(input('Enter side c:'))
perimeter= (side_a + side_b + side_c)
print('Perimeter of a triangle:', perimeter)


# In[6]:


# question 6
#Get length and width of a rectangle using prompt. Calculate its area (area = length x
#width) and perimeter (perimeter = 2 x (length + width)). say length=4, width=5
length = int(input('Enter length:'))
width = int(input('Enter widht:'))
area= (length*width)
print(area)


# In[7]:


#Question 7
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
#circumference (c = 2 x pi x r) where pi = 3.14. say r=3

r=3
area=3.14*r*r
c=2*3.14*r
print('Circumference:', c)
print('Area:', area)


# In[32]:


#Calculate the slope, x-intercept and y-intercept of y = 2x -2
#with the expression y=mx+b,
#to find slope
#Assuming,x=4
x=4
y=(2*x)-2
print('Coordinate of Y:', y)
print('Coordinate of X:', x)
m=(y-b)/x
print('Slope:', m)
b=y-(m*x)
print('Y intercept:', b)
# to find X intrcept make y 0
x=(b-0)/m
print('X intercept:', x)


# In[35]:


# Question 9
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2)
# and point (6,10)
x1=2
x2=6
y1=2
y2=10
m1=(y2-y1)/(x2-x1)
print('Slope:', m1)

#Find an Euclidian distance between (2, 2) and (6, 10)

import math
x= (2,2)
y= (6, 10)
distance= math.sqrt(sum([(a-b)**2 for a, b in zip(x,y)]))
print("Euclidian distance from x to y:", distance)


# In[36]:


# question 10. Compare the slopes in tasks 8 and 9.
print(m==m1)


# In[8]:


# Find the length of 'python' and 'dragon' and make a falsy comparison statem
len('python')


# In[9]:


len('dragon')


# In[10]:


len('python')==len('dragon')


# In[11]:


len('python')!=len('dragon')


# In[13]:


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in Dragon', 'on' in 'dragon') 
print('on in Python', 'on' in 'python') 
print('on in Dragon', 'on' in 'dragon') and print('on in Python', 'on' in 'python') 
print('on in Dragon and Python', 'on' in 'dragon' and 'on' in 'python') 


# In[14]:


# I hope this course is not full of jargon. Use in operator to check if jargon is in the
#sentence.
print('jargon is in the sentence', 'jargon' in 'I hope this course is not full of jargon')


# In[15]:


# There is no 'on' in both dragon and python
print('on' not in 'dragon' and python)


# In[16]:


# Find the length of the text python and convert the value to float and convert it to
#string
print(float(len('python')))
print(str(len('python')))


# In[17]:


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a
#number is even or not using python?
num=int(input('Enter a number to tes if its odd or even:'))
if (num%2)==0:
    print('The number is even')
else:
    print('The number is odd')


# In[18]:


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
7//3==int(2.7)


# In[19]:


#  Check if type of '10' is equal to type of 10
'10'==10


# In[20]:


# Check if int('9.8') is equal to 10
int(9.8)==10


# In[21]:


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of
#the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
hours=int(input('Hours worked:'))
rate_per_hour=int(input('Rate per hours worked'))
weekly_earning = hours*rate_per_hour
print('Pay of the person:', weekly_earning)


# In[22]:


# Write a script that prompts the user to enter number of years. Calculate the number
# of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years=int(input('Enter your age:'))
year_in_s=3153600000
scbl=years*year_in_s
print('Seconds livabe:', scbl)


# In[23]:


#  Write a Python script that displays the following table
# 1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




