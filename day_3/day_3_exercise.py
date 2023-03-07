# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:18:04 2023

@author: manCom
"""

my_age=31
print(my_age)
my_height=6.5
print('My age is', my_age, 'years')
print('my height:', my_height, 'm')
complex_number=1+2j
print('Complex number:', complex_number)
complex_number= (1+2j)
print('Complex number:', complex_number)
base=20
height=10
print('Area:', 0.5*base*height)
side_a=5
side_b=4
side_c=3
print('perimeter:', side_a+side_b+side_c )
length=10
width=7
print('area:', length*width)
print('perimeter:', 2*(length+width))
radius=2
print('area:', 3.14*2*radius)
print('c:', 2*3.14*radius)
#y=2x-2
#if x=8

x=8
y=(2*x-2)
print(y)

 #slope m=y2-y1/x2-x1
x1=2
x2=2
y1=6
y2=10 
slope=(y2-y1)/(x2-x1)




distance= math.sqrt(sum([(a-b)**2 for a, b in zip(x,y)]))
print("Euclidian distance from x to y:", distance)

