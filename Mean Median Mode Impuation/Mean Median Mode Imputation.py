#!/usr/bin/env python
# coding: utf-8

# ## Mean Median Mode Imputation : 

# Mean, median, and mode imputation are techniques used in data preprocessing to handle missing data in a dataset. They involve replacing missing values with the mean, median, or mode of the available data in the respective column. Each method has its own advantages and is applicable in different scenarios:
# 
# 1. Mean Imputation:
#    - In mean imputation, missing values are replaced with the mean (average) value of the non-missing data in the column.
#    - This method is suitable for continuous numerical data, such as age, income, or temperature, where the distribution of values is approximately normal.
#    - Mean imputation can distort the original data distribution if the missing values are not missing completely at random (MCAR). It tends to pull the data towards the center of the distribution.
# 
# 2. Median Imputation:
#    - Median imputation replaces missing values with the median value, which is the middle value when the data is sorted in ascending order.
#    - This method is more robust to outliers compared to mean imputation, making it suitable for data with skewed or non-normal distributions.
#    - It is a better choice when the data contains outliers because outliers can significantly affect the mean.
# 
# 3. Mode Imputation:
#    - Mode imputation is used for categorical or nominal data. It replaces missing values with the most frequent category (mode) in the column.
#    - This method is appropriate for data like color, nationality, or product type, where the concept of mean or median is not meaningful.
#    - Mode imputation is often used when dealing with categorical data, but it may not be suitable for continuous data.
# 

# In[1]:


import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')


# In[2]:


dataframe = pd.read_csv('Titanic.csv')


# In[3]:


dataframe.head()


# In[4]:


dataframe.tail()


# In[5]:


dataframe.shape


# In[6]:


dataframe.info()


# In[7]:


dataframe.select_dtypes(include = 'object').head()


# In[8]:


dataframe.isna().sum().any()


# In[9]:


dataframe.isna().sum()


# In[10]:


dataframe['Age'].describe()


# If you have a dataset with an "Age" column, and some of the entries in that column are missing or marked as "NaN" (which stands for "Not-a-Number"), replace those missing values with the average age of all the people.
# 
# Here's how you can do it:
# 
# 1. Calculate the mean (average) age of all the people in your dataset.
# 2. Then, go through the "Age" column, and wherever you find a missing or "NaN" value, replace it with the calculated mean age.
# 
# 

# In[11]:


dataframe_2 = dataframe.copy()


# In[12]:


dataframe_2.head()


# In[13]:


mean = dataframe_2['Age'].mean()


# In[14]:


mean


# In[15]:


dataframe_2['Age'] = dataframe_2['Age'].fillna(mean)


# In[16]:


dataframe_2['Age'].isna().sum()


# If you have a feature, like "Age," in your dataset, and some values are missing (NaN), replacing those missing values with the median is a good idea when the data doesn't follow a normal or Gaussian distribution. 
# 
# Here's how to do it in simple terms:
# 
# 1. Calculate the median age from the available data in the "Age" feature. The median is the middle value when all the ages are sorted from smallest to largest.
# 
# 2. Replace all the missing (NaN) ages in the "Age" feature with this calculated median age.
# 

# In[17]:


dataframe_3 = dataframe.copy()


# In[18]:


dataframe_3.head()


# In[19]:


dataframe_3.isna().sum()


# In[20]:


median = dataframe_3['Age'].median()


# In[21]:


median


# In[24]:


dataframe_3['Age'] = dataframe_3['Age'].fillna(median)


# In[25]:


dataframe_3['Age'].isna().sum()


# You can replace missing values in the "Age" feature with the mode, which is the most frequent value in the dataset. In your example, if 17 is the most common age, you can assume that missing ages are also 17:
# 
# 1. Find the mode (most frequent age) in the "Age" feature.
# 2. Replace all the missing (NaN) ages in the "Age" feature with this mode age.
# 

# In[26]:


dataframe_4 = dataframe.copy()


# In[27]:


dataframe_4.isna().sum().any()


# In[28]:


dataframe_4.isna().sum()


# In[30]:


mode = dataframe_4['Age'].mode()[0]


# In[31]:


mode


# In[32]:


dataframe_4['Age'] = dataframe_4['Age'].fillna(mode)


# In[33]:


dataframe_4.isna().sum().any()


# In[34]:


dataframe_4.isna().sum()


# In[ ]:




