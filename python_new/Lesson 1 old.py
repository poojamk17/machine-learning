#!/usr/bin/env python
# coding: utf-8

# # Heading1
# ## Heading2
# ### Heading3
# #### Heading4
# ###### Heading5
# akjalsksjk

# In[1]:


# know your current directory
get_ipython().run_line_magic('pwd', '')


# In[8]:


print("Hello World")


# In[6]:


# know the python version
import sys
print(sys.version)


# ## Mathemamtical Calculations

# In[12]:


# Addition
3+4


# In[13]:


# Subtraction
3-4


# In[14]:


# Multiplication
3*4


# In[15]:


# Division
3/4


# In[16]:


# Modulus
3%4


# In[17]:


# Floor Division
3//4


# In[18]:


# BODMAS
3+4+7*8-4/2


# In[19]:


import math
print(math.sqrt(9))


# In[20]:


# Square Root
9**(1/2)


# In[21]:


# Cube Root
27**(1/3)


# ## Data Types
# int
# 
# float
# 
# bool
# 
# str
# 
# datetime
# 
# enumerate

# In[29]:


a=2
a


# In[33]:


type(a)


# In[24]:


a


# In[65]:


b=4.5
type(b)


# In[66]:


a=3.5


# In[67]:


type(a)


# In[68]:


b = int(a)


# In[69]:


b


# In[70]:


a+b


# In[71]:


b+True


# In[72]:


3.5 + b + True


# In[74]:


c="data"
c


# In[75]:


type(c)


# In[76]:


d = float(c)


# In[82]:


e = '3.5'
type(e)


# In[83]:


f = float(e)
f


# In[85]:


m = '3'


# In[86]:


n = int(m)
n


# In[87]:


3.4 + int('3') + True


# In[88]:


int(True)


# In[89]:


float(True)


# In[90]:


str(True)


# In[91]:


bool('False')


# In[92]:


bool(1)


# In[93]:


bool(0)


# In[94]:


bool('')


# In[1]:


bool(False)


# In[2]:


bool(True)


# In[3]:


s = "i am a Data Scientist"
type(s)


# In[4]:


len(s)


# # Assignment Operator

# In[5]:


a = 5
a = a+4


# In[6]:


a


# In[8]:


a += 4


# In[9]:


a


# In[10]:


a -= 3


# In[11]:


a


# In[12]:


b =2
a *= b
a


# In[13]:


a **= 2


# In[14]:


a


# In[15]:


5<7


# In[16]:


5<7 and not 7>8


# In[17]:


my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)


# In[18]:


s = "My name is Narayana Swamy"


# In[19]:


len(s)


# In[20]:


for i in s:
    print(i)


# In[21]:


s[0]


# In[22]:


s[0,8]


# In[23]:


s[0:8]


# In[24]:


s[::-1]


# In[25]:


s[-1]


# In[26]:


s[-1:]


# In[27]:


s[0:6]


# In[28]:


s[0:7]


# In[29]:


s.upper()


# In[30]:


s.lower()


# In[31]:


s.capitalize()


# In[32]:


s.title()


# In[33]:


s.split()


# In[34]:


s.split('M')


# In[41]:


name = 'swamy'
age = 30
print('my name is {} and age is {}'.format(name,age))


# In[43]:


name1 = 'Bangalore'
name2 = 'Mysore'
d = 150
print('the distance between {} and {} is {}'.format(name1,name2,d))


# In[50]:


s1 = 'My'
s2 = 'Name'
s3 = '23'


# In[51]:


s1+s2+s3


# In[52]:


s1*5


# # list
# 

# In[53]:


lit=[]


# In[54]:


type(lit)


# In[55]:


len(lit)


# In[63]:


lst=['name is',20,2.6,'0']


# In[64]:


list=lst


# In[65]:


list


# In[66]:


list[0]


# In[67]:


list[:2]


# In[68]:


list[0:2]


# In[69]:


list[0][5:]


# In[70]:


#use split function and get the domain name
email='pooja.mk@testyantra.in'


# In[75]:


b=email.split('@')
b


# In[76]:


b=email.split('@')[1]
b


# In[77]:


a=[2,3,4,5]
b=[6,7,8,9]
a+b


# In[78]:


a-b


# In[79]:


a*b


# In[80]:


a*2


# In[81]:


a.append(10)


# In[82]:


a


# In[83]:


a.extend(2)


# In[84]:


a.extend([2])


# In[85]:


a.extend([0,9,8])


# In[86]:


a


# In[87]:


a.insert(3,'pooja')
a


# In[88]:


a.clear(0)
a


# In[89]:


a.clear
a


# In[90]:


a.clear()
a


# In[91]:


p=[1,2,3,4,5]


# In[92]:


p.copy()


# In[93]:


c=p.copy()


# In[94]:


c


# In[95]:


nl=[2,3,4,['po',1],'mk',[9,8,7]]


# In[96]:


nl[3][1]


# In[100]:


nl[3][0]


# In[103]:


del(p)


# In[106]:


n=[1,2,3['po',1,['mk',9,9]]]


# In[107]:


a=10
b=str(a)


# In[108]:


b


# # dictinory

# In[111]:


d={"name":"pooja",
    "age":22
     }


# In[112]:


d1


# In[113]:


d1={"name":["pooja","kavya","moulya","mamatha"],
   "age":[21,20,22,19],
   "course":["a","b","c","c"]}


# In[114]:


d1


# In[115]:


d1["name"]


# In[116]:


d1["age"]


# In[117]:


d1["name","age"]


# In[118]:


d1["age"][3]


# In[119]:


d1.items()


# In[120]:


d1.keys()


# In[121]:


type(d1)


# In[122]:


d1.update("upadte":[1,2,3])
d1


# # tuples

# In[128]:


tup1=(1,2,3,4,2,4,3,5)
tup1


# In[124]:


type(tup1)


# In[125]:


tup1[3]


# In[126]:


tup1[3]=100


# In[129]:


tup1.count(2)


# In[130]:


tup1.index(10,2,3)


# # sets

# In[133]:


s1={2,3,4,5,5,5,5,5,5,5,6}


# In[134]:


s1


# In[135]:


s2={1,2,3,4,5,1,2,3,4,5,1,2,3,4,5}
s1


# In[136]:


s1.intersection(s2)


# In[137]:


s1.union(s2)


# In[138]:


s1.difference()


# In[ ]:


a

