#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[2]:


dataframe = pd.read_csv('House Price.csv')


# In[3]:


dataframe.head()


# In[4]:


dataframe.tail()


# In[6]:


pd.set_option('display.max_rows',100)
dataframe.isnull().sum().sort_values()


# ## Frequent Category Imputation :

# Frequent Category Imputation is a technique used to fill in missing information in a dataset. Here's how it works in simple language:
# 
# 1. Find missing values percentage: First, we need to figure out how much data is missing in our dataset. This means finding out what proportion of the information is incomplete or not available.
# 
# 2. Check missing values percentage is less than 20%: We want to make sure that the missing data isn't too extensive. So, we check if the percentage of missing data is less than 20%. If it's higher than that, we might consider other methods because a large amount of missing data can impact the quality of our analysis.
# 
# 3. Then replace missing values with most frequent category / Mode: If the missing data is less than 20%, we can go ahead and fix it. We replace the missing values with the category or option that appears most frequently in that particular column. This is called the "mode." By doing this, we are making an educated guess based on the most common data in that column.
# 
# Frequent Category Imputation is a simple way to fill in missing data by using the most popular category in a column, but it's only suitable when the amount of missing data is relatively small, less than 20%.

# In[7]:


pd.set_option('display.max_rows',100)
dataframe.isnull().mean().sort_values()


# In[8]:


plt.figure(figsize=(12,6))
dataframe.isnull().sum().plot(color='r')


# In[10]:


for col in dataframe.columns:
    if dataframe[col].isnull().mean() <= 0.20:
        dataframe[col].fillna(dataframe[col].mode()[0], inplace = True)


# In[11]:


plt.figure(figsize = (12,6))
dataframe.isnull().sum().plot(color = 'r')


# ### 1. Finding feature which is having more than 20% NaN values

# In[12]:


features = []
for feature in dataframe.columns:
    if dataframe[feature].isnull().mean() > 0.20:
        features.append(feature)


# In[13]:


for i in features:
    print(('{} having     {}% null values').format(i,dataframe[i].isnull().mean()))


# ### 2. Capture NaN with New variable

# Replace NaN with 'Missing'

# In[14]:


for col in features:
    dataframe[col].fillna('Missing',inplace=True)


# In[15]:


for i in features:
    print(('{} having     {}% null values').format(i,dataframe[i].isnull().mean()))


# In[16]:


plt.figure(figsize = (12,6))
dataframe.isnull().sum().plot(color = 'g')


# In[18]:


import missingno as mn
mn.matrix(dataframe)


# ###  3. Capturing NaN with new feature

# Replace NaN with 1 else 0

# In[19]:


dataframe = pd.read_csv('House Price.csv',usecols=features)
dataframe.head()


# In[20]:


dat=[]
for col in dataframe.columns:
    dataframe[col+'_New']=np.where(dataframe[col].isnull(),1,0)
    dat.append(col+'_New')


# In[21]:


dat


# In[22]:


dataframe.head()


# In[23]:


plt.figure(figsize = (12,6))
dataframe.isnull().sum().plot(color = 'g',marker = 'o')
dataframe[dat].isnull().sum().plot(color = 'r',marker = '^')


# In[ ]:




