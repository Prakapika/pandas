#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
#Assign it to a variable called users and use the 'user_id' as index

users=pd.read_csv(r'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user')
users['user_id']=users['user_id|age|gender|occupation|zip_code'].apply(lambda x:x.split('|')[0])
users['age']=users['user_id|age|gender|occupation|zip_code'].apply(lambda x:int(x.split('|')[1]))
users['gender']=users['user_id|age|gender|occupation|zip_code'].apply(lambda x:x.split('|')[2])
users['occupation']=users['user_id|age|gender|occupation|zip_code'].apply(lambda x:x.split('|')[3])
users['zip_code']=users['user_id|age|gender|occupation|zip_code'].apply(lambda x:x.split('|')[4])
users.drop('user_id|age|gender|occupation|zip_code',axis=1,inplace=True)
users.set_index('user_id',inplace=True)
users


# In[3]:


users.head(10)


# In[4]:


users.tail(10)


# In[5]:


#What is the number of observations in the dataset?
len(users)


# In[6]:


#What is the number of columns in the dataset?
len(users.columns)


# In[7]:


#Print the name of all the columns.
users.columns


# In[8]:


#How is the dataset indexed?
users.index


# In[9]:


#What is the data type of each column?
result=users.info()
result


# In[10]:


#Print only the occupation column
users.occupation


# In[11]:


#How many different occupations are in this dataset?
count = users.occupation.unique().size
count


# In[12]:


#What is the most frequent occupation?
users['occupation'].mode()


# In[13]:


#DataFrame Info.
users.info()


# In[14]:


#Describe all the columns
users.describe()


# In[15]:


#Summarize only the occupation column
users.groupby('occupation')['occupation'].count()


# In[16]:


#What is the mean age of users?
users['age'].mean()


# In[17]:


#What is the age with least occurrence?
users['age'].value_counts().idxmin()


# In[ ]:




