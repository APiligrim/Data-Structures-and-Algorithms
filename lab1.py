#!/usr/bin/env python
# coding: utf-8

# ### Anastasiya Uraleva 
# #### Lab 1 Submission: Python Concepts Lab

# In[ ]:


The object of this lab is to get all the `asserts` to evaluate to `True`


# In[1]:


x = 2 > 1
# solution: x = 2 > 1


# In[2]:


assert x is True


# ### Strings

# 1. Some string methods
# 
# Reference: https://docs.python.org/3/library/stdtypes.html#string-methods

# In[42]:


original = ' Python strings are COOL! '

lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.strip().lower()


# In[43]:


assert lower_cased == ' python strings are cool! '
assert stripped == 'Python strings are COOL!'
assert stripped_lower_cased == 'python strings are cool!'


# 2. String interpolation

# In[5]:


# Given the following:
verb = ' is '
language = ' Python '
punctuation = '!'


# In[57]:


# Construct "sentence"
sentence = 'Learning' + language + verb + 'fun' + punctuation
assert sentence == 'Learning Python is fun!'


# ### Numbers

# \begin{align}
#  result = 6a^3 - \frac{8b^2 }{4c} + 11
# \end{align}

# In[7]:


a = 2
b = 3
c = 2


# In[215]:


# Your formula here:
result = 6*pow(a,3)-(8*pow(b,2))/(4*c)+11


# In[214]:


assert result == 50


# ### Lists

# In[63]:


# Let's create an empty list
my_list = []

# Let's add some values
my_list.append('Python')
my_list.append('is ok')
my_list.append('sometimes')

print(my_list)


# In[64]:


assert len(my_list) == 3


# In[72]:


print(my_list)

# Let's remove 'sometimes'
my_list.remove('sometimes')

# Let's change the second item
my_list[-1] = 'is neat'


# In[73]:


assert my_list == ['Python', 'is neat']


# Create a new list without modifiying the original one

# In[129]:


original = ['I', 'am', 'learning', 'hacking', 'in']
print(original)


# In[141]:


modified = original[:]
modified_final = modified


modified_final.remove('hacking')
modified_final.insert(3, 'lists')
modified_final.insert(5, 'Python')
print(modified_final)
print(original)


# In[142]:


assert original == ['I', 'am', 'learning', 'hacking', 'in']
assert modified == ['I', 'am', 'learning', 'lists', 'in', 'Python']


# Merge two lists

# In[17]:


list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]


# In[82]:



my_list = list1 + list2 + list3
my_list.sort(reverse=True)
print(my_list)


# In[81]:


print(my_list)
assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]


# ### Dictionaries

# In[20]:


first_name = 'John'
last_name = 'Doe'
favorite_hobby = 'Python'
sports_hobby = 'gym'
age = 82


# In[146]:


# Your implementation
my_dict = {
        'first_name': 'John',
        'last_name':'Doe', 
        'favorite_hobby':'Python', 
        'sports_hobby':'gym',
        'age': '82'
        }


# In[149]:


assert my_dict['first_name'] == 'John'
assert my_dict['last_name'] =='Doe'
assert my_dict['favorite_hobby']=='Python'
assert my_dict['sports_hobby']=='gym'
assert my_dict['age']=='82'


# ### Loops

# In[218]:


words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
upper_case_words = []

for word in words:
    if word.isupper():
        upper_case_words.append(word)        


# In[217]:


assert upper_case_words == ['PYTHON', 'JOHN', 'DOE']


# ### Functions

# In[219]:


# Fill ____ pieces of the count_even_numbers implemention in order to pass the assertions. You can assume that numbers argument is a list of integers.

def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# In[220]:


assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4


# Implement `find_wanted_people` function which takes a list of names (strings) as argument. The function should return a list of names which are present both in WANTED_PEOPLE and in the name list given as argument to the function.

# In[227]:


WANTED_PEOPLE = ['John Doe', 'Clint Eastwood', 'Chuck Norris']


# In[230]:


def find_wanted_people(names):
    wanted_names = []
    for name in names:
        if name in WANTED_PEOPLE:
            wanted_names.append(name)
    return wanted_names


# In[231]:


people_to_check1 = ['Donald Duck', 'Clint Eastwood', 'John Doe', 'Barack Obama']
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert 'John Doe' in wanted1
assert 'Clint Eastwood'in wanted1

people_to_check2 = ['Donald Duck', 'Mickey Mouse', 'Zorro', 'Superman', 'Robin Hood']
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []


# In[ ]:




