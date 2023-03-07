# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:53:32 2023

@author: manCom
"""

# Exercise: Level 1

# 1. Check the python version you are using

# 2 Open the python interactive shell and do the following operations. The operands are 3 and 4. 
3+4
3-4
3*4
3%4
3/4
3**4
3//4

# 3 Write strings on the python interactive shell. The strings are the following
print('Hassan')
print('Sani')
print('Nigeria')
print('I am enjoying 30 days of python')

# Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Hassan'))
print(type('Sani'))
print(type('Ngeria'))

# Exercise: Level 3
# 1 Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary. 
print(type(3)) #for intergers
print(type(3.3)) # fro float
print(print("HASSAN")) # fro string
print(type((3.5, 1.9, 3.6))) # for tuple
print(type({3.5, 1.9, 3.6})) # for set
print(type({'name':'Hassan'})) # for Dictionary
print(type(3.5 + 4j))      # Complex number

# 2. Find an Euclidian distance between (2, 3) and (10, 8)
import math
x= (92,3)
y= (10, 8)
distance= math.sqrt(sum([(a-b)**2 for a, b in zip(x,y)]))
print("Euclidian distance from x to y:", distance)
