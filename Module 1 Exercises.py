#!/usr/bin/env python
# coding: utf-8

# # Chapter 1 - Exercises

# #### 1- Define a variable and assign it your first name (bonus points for input command!)  
# #### <em>(Hint: Use the contents covered in the first module, feel free to [check it](https://github.com/LongOnly/Training/blob/master/Module%201.ipynb))</em>

# In[1]:


name = input()


# In[ ]:





# #### 2- Retrieve the last 3 characters of your name, assign it to a new variable

# In[2]:


l3=name[-3:]
l3


# In[ ]:





# #### 3- Add the first 3 characters of your name to the end of the previous variable, make it upper case then capitalize it

# In[3]:


f3plus=l3+name[:3]
f3plus


# #### 4- Create a new variable with the year of your birth (its ok to lie here)

# In[4]:


DOB=input()


# #### 5- Join your name (in lower case) and the last 2 digits of your year of birth into the same variable

# In[5]:


joined=name.lower()+str(DOB[-2:])
joined


# #### 6- Use the previous variable, multiply the digits by 2

# In[6]:


mjoined=name+str(int(DOB[-2:])*2)
mjoined


# In[10]:


number=(int(DOB[-2:])*2)
number


# In[ ]:





# #### 7- Create an if statement, if that number is superior or equall to 178, print "you are 30 years old or younger", else print "you are 30 years old or older"

# In[12]:


comp=(number>=178)
comp


# In[15]:


if comp:print("you are 30 years old or younger")
else:print("you are 30 years old or older")


# #### 8- Replace in the following string the following characters: 0 by o and 3 by e  
# Then add " - Exercises" to it

# In[16]:


ReplaceMe = "Pyth0n Crash C0urs3 M0dul3 1"


# In[17]:


ReplaceMe=ReplaceMe.replace("0","o").replace("3","e")+"- Exercise"
ReplaceMe


# #### 9- Join all the variables from the previous exercises with a ";" between each then split them by ";"

# In[19]:


(name+";"+l3+";"+f3plus).split(";")


# In[ ]:





# #### 10- There's a column from an excel file that we currently receive monthly that we want to extract, however its name is inconsistent. For example, the last 2 months it has been named 'SalesFiGuRES   ' and 's AL Es'
# 
# #### However we expect it to always mention the word 'sales', find a way to describe the name of that column in a way that we can always find the correct column

# In[24]:


name1 = 'SalesFiGuRES   '
name1=name1.lower().replace(" ","")
name1


# In[27]:


name2 = 's AL Es'
name2=name2.lower().replace(" ","")
name2


# In[29]:


if 'sales' in (name1):print('We found the correct column')


# In[30]:


if 'sales' in (name2):print('We found the correct column')

