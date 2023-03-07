#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating a string
letter = 'P' # A string could be a single character or a bunch o
print(letter) # P
print(len(letter)) # 1
greeting = 'Hello, World!' # String could be made using a single or double quo
print(greeting) # Hello, World!
print(len(greeting)) # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)


# In[4]:


# Multiline string is created by using triple single (''') or triple double quotes ("""). See the
#example below.
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing


multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)


# In[ ]:


# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)


# In[7]:


# string concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name)) # 8
print(len(last_name)) # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
# sum the lengths of 2 strings
print(len(first_name) + len(last_name))
# divide the lengths of a string by another
print(len(first_name) / len(last_name))


# In[10]:


# Escape Sequences in Strings
# In Python and other programming languages \ followed by a character is an escape
# sequence. Let us see the most common escape characters:
#\n: new line
#\t: Tab means(8 spaces)
#\\: Back slash
#\': Single quote (')
#\": Double quote (")


# In[3]:


print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line br
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to w
print('In every programming language it starts with "Hello, World!"') # to w


# In[4]:


#Old Style String Formatting (% Operator)
#In Python there are many ways of formatting strings. In this section, we will cover some of
#them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed
#size list), together with a format string, which contains normal text together with
#"argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#"%.number of digitsf" - Floating point numbers with fixed precision
#New Style String Formatting (str.format)
#This formatting is introduced in Python version 3.
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)


# In[7]:


first_name='Hassan'
last_name='Sani'
language='snake'
formated_string='I am %s %s. I teach %ss' %(first_name, last_name, language)
print(formated_string)


# In[9]:


# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask


# In[11]:


#New Style String Formatting (str.format)
#This formatting is introduced in Python version 3.
first_name='Hassan'
last_name='Sani'
language='snake'
formated_string='I am {} {} I teach {}'.format(first_name, last_name, language)
print(formated_string)


# In[18]:


a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after d
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# In[25]:


# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, pi, pi*radius)
print(formated_string)


# In[36]:


#String Interpolation / f-Strings (Python 3.6+)
#Another new string formatting is string interpolation, f-strings. Strings start with f and we
#can inject the data in their corresponding positions.
a = 4
b = 3
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b:.2f}') # to 2 decimal place
print(f'{a}+{b}={a+b}')
print(f'{a}//{b}={a//b}')
print(f'{a}%{b}={a%b}')
print(f'{a}**{b}={a**b}')


# In[ ]:


#Python Strings as Sequences of Characters
#Python strings are sequences of characters, and share their basic methods of access with
#other Python ordered sequences of objects – lists and tuples. The simplest way of
#extracting single characters from strings (and individual members from any sequence) is to
#unpack them into corresponding variables.


# In[38]:


#Unpacking characters
language='Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


# In[58]:


#Accessing Characters in Strings by Index
#In programming counting starts from zero. Therefore the first letter of a string is at zero
#index and the last letter of a string is the length of a string minus one.
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n


# In[59]:


#If we want to start from right end we can use negative indexing. -1 is the last index.
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o


# In[68]:


# Slicing Python Strings
# In python we can slice strings into substrings.
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three) # hon
last_three = language[3:]
print(last_three) # hon


# In[67]:


#Reversing a String
# We can easily reverse strings in python by using [::-1].
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH


# In[83]:


greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
print(len(greeting))


# In[89]:


#Skipping Characters While Slicing
#It is possible to skip characters while slicing by passing step argument to slice method.
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto


# In[4]:


#String Methods
#There are many string methods which allow us to format strings. See some of the string
#methods in the following example:
#capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'


# In[6]:


#count(): returns occurrences of substring in string, count(substring, start=.., end=..).
#The start is a starting indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2`


# In[7]:


#endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False


# In[11]:


#expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) # 'thirty days of python'
print(challenge.expandtabs(10)) # 'thirty days of python'


# In[18]:


# find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0
print(challenge.find('t')) #0
print(challenge.find('tho')) #17


# In[20]:


# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y')) # 16
print(challenge.rfind('th')) # 17


# In[29]:


# format(): formats string into a nicer output
# More about string formatting check this link
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I


radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314


# In[41]:


#index(): Returns the lowest index of a substring, additional arguments indicate starting
#and ending index (default 0 and string length - 1). If the substring is not found it raises
#a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7
print(challenge.index(sub_string, 9)) # error


# In[33]:


#rindex(): Returns the highest index of a substring, additional arguments indicate
#starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 7
print(challenge.rindex(sub_string, 9)) # error


# In[42]:


# salnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True
challenge = '30DaysPython'
print(challenge.isalnum()) # True
challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character
challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False


# In[43]:


# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha()) # False


# In[44]:


#isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal()) # False
challenge = '123'
print(challenge.isdecimal()) # True
challenge = '\u00B2'
print(challenge.isdigit()) # False
challenge = '12 3'
print(challenge.isdecimal()) # False, space not allowed


# In[45]:


# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode
#characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit()) # True
challenge = '\u00B2'
print(challenge.isdigit()) # True


# In[46]:


#isnumeric(): Checks if all characters in a string are numbers or number related (just like
#isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False


# In[47]:


#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# In[48]:


#slower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False


# In[55]:


#isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# In[65]:


# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result =' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


# In[73]:


#strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'


# In[74]:


#replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'


# In[75]:


#split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']   


# In[76]:


#title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python


# In[77]:





# In[79]:


# startswith(): Checks if String Starts with the Specified String
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
print(challenge.startswith('30')) # True


# In[ ]:




