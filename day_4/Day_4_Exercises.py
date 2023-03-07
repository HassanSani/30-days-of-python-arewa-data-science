#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 1.
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of
# Python'.
new_sring=['Thirty', 'Days', 'Of', 'Python']
result=' '.join(new_sring)
print(result)


# In[8]:


#Q 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
new_sring=['Coding', 'For' , 'All']
result=' '.join(new_sring)
print(result)


# In[15]:


#Q3-8. Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"
print(company)
print(len(company))
#  Change all the characters to uppercase letters using upper() method and lower case using lower() method.
print(company.upper()) # CODING FOR ALL
print(company.lower()) # coding for all


# #Q9. Use capitalize(), title(), swapcase() methods to format the value of the string Coding
# #For All.
# 

# In[18]:


# Q8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding
#For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())


# In[28]:


#Q9. Cut(slice) out the first word of Coding For All string.
company="Coding For All"
first_word_sliced=company[6:14]
print(first_word_sliced)

#Q10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')) 
print(company.index('Coding')) 

# Q 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python')) 


# In[39]:


# 12. Change Python for Everyone to Python for All using the replace method or other methods.
companion='Python for Everyone'
print(companion.replace('Everyone', 'All'))
# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(companion.split())
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
social_media= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(social_media.split(','))


# In[54]:


#Q15 What is the character at index 0 in the string Coding For All.
companion='Python for All'
index_0=companion [0]
print(index_0)

#Q16. What is the last index of the string Coding For All.\
last_index=len(companion)-1
print(last_index)
#Q17. What character is at index 10 in "Coding For All" string.
index_10=companion[10]
print(index_10) # a ' '


# In[60]:


#Q18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
company='Python For Everyone'
abbreviation=company.replace('Python For Everyone','PFE')
print(abbreviation)


# In[61]:


#Q19. Create an acronym or an abbreviation for the name 'Coding For All'.
companion='Python For All'
abbreviation=companion.replace('Python For All','PFA')
print(abbreviation)


# In[65]:


# 20. Use index to determine the position of the first occurrence of C in Coding For All.
company='Coding For All'
print(company.find('C'))
# 21. Use index to determine the position of the first occurrence of F in Coding For All
print(company.find('F'))
#print(company.find('C'))
print(company.rfind('C'))


# In[93]:


#23. Use index or find to find the position of the first occurrence of the word 'because' in 
#the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#24. Use rindex to find the position of the last occurrence of the word because in the
#following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print(sentence.rfind('because'))

# Slice out the phrase 'because because because'
print(sentence.replace('because because because','')) 
a=(sentence[0:31])
b=(sentence[-16:])
print(a+b)


# In[95]:


#Q28. Does ''Coding For All' start with a substring Coding?
coding='Coding For All'
print(coding.startswith('Coding'))
#29. Does 'Coding For All' end with a substring coding?
print(coding.endswith('Coding'))


# In[98]:


# remove spaces' Coding For All '
print(coding.strip(' '))


# In[104]:


#Q31 Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
coding='30DaysOfPython'
print(coding.isidentifier())
#thirty_days_of_python='30DaysOfPython'
codings='thirty_days_of_python'
print(codings.isidentifier())


# In[107]:


# Q32. The following list contains the names of some of python libraries: ['Django', 'Flask',
#'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries= ['Django', 'Flask','Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)


# In[110]:


#  Use the new line escape sequence to separate the following sentences
#I am enjoying this challenge.
#I just wonder what is next.

print('I am enjoying this challenge. \nI just wonder what is next.')


# In[114]:


#Name Age Country City
#Asabeneh 250 Finland Helsinki
print('Name\t\tAge\tCountry \tCity\nAsabeneh \t250 \tFinland \tHelsinki')


# In[128]:


# . Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
formated_string='The area of a circle with {} is {}'.format(radius, area) +' '+ 'meters square'
print(formated_string)


# In[134]:


#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a=8
b=6
print('{}+{}={}'.format(a,b, a+b))
print('{}-{}={}'.format(a,b, a-b))
print('{}*{}={}'.format(a,b, a*b))
print('{}/{}={:.2f}'.format(a,b, a/b))
print('{}%{}={}'.format(a,b, a%b))
print('{}//{}={}'.format(a,b, a//b))
print('{}**{}={}'.format(a,b, a**b))


# In[ ]:




