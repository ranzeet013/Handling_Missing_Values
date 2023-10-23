#!/usr/bin/env python
# coding: utf-8

# ## Missingness Indicator :

# A missingness indicator, also known as a missing data indicator, is a binary variable created to identify whether a particular data point in a dataset is missing or not for a specific feature or attribute. It is used to flag the presence or absence of missing values in a dataset. Missingness indicators are often used to handle and analyze missing data systematically.
# 
# Here are some key points about missingness indicators:
# 
# 1. **Purpose**: Missingness indicators are created to help manage and analyze missing data in a dataset. They serve as a flag to indicate whether a particular data point is missing or not.
# 
# 2. **Binary Variable**: A missingness indicator is a binary variable that typically takes on one of two values:
#    - 1: Indicates that the data is missing for a specific data point.
#    - 0: Indicates that the data is not missing, i.e., it is present and has a valid value.
# 
# 3. **Creation**: For each feature or attribute in the dataset with missing values, a corresponding missingness indicator is created. These indicators are calculated based on the presence or absence of missing data in that particular feature.
# 
# 4. **Use**: Missingness indicators can be used in statistical analyses, machine learning models, or other data-related tasks to account for and handle missing data appropriately. They provide a structured way to incorporate the information about missing values into the analysis.
# 
# 5. **Example**: Let's say you have a dataset with information about customers, and one of the features is "Email Address." You can create a missingness indicator for this feature. If a customer has an email address recorded, the indicator is set to 0 (no missing data); if the email address is missing, the indicator is set to 1 (missing data).
# 
# 6. **Benefits**: Missingness indicators help prevent bias in data analysis caused by ignoring missing values. They allow you to consider the missing data systematically, either by excluding, imputing, or analyzing it based on the nature of your study.
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[2]:


dataframe = pd.read_csv('Titanic.csv', usecols = ['Age', 'Fare', 'Survived'])


# In[3]:


dataframe.head()


# In[4]:


dataframe.tail()


# In[6]:


dataframe.shape


# In[7]:


dataframe.info()


# In[8]:


dataframe.isna().sum().any()


# In[9]:


dataframe.isna().sum()


# In[10]:


dataframe.isna().mean()


# In[14]:


import missingno as mn

mn.matrix(dataframe)


# There is 177 NaN values are present in Age feature it is approximately 20%

# In[15]:


dataframe['Age_NaN'] = np.where(dataframe['Age'].isnull,0,1)


# Create a missingness indicator feature named 'Age_NaN' in dataset. This feature is designed to indicate the presence or absence of missing values (NaN values) in the 'Age' feature. The 'Age_NaN' feature is structured as follows:
# 
# - When the 'Age' feature has a missing value (NaN), the corresponding 'Age_NaN' value is set to 1.
# - When the 'Age' feature has a valid value (not missing), the 'Age_NaN' value is set to 0.
# 
# This 'Age_NaN' feature provides a convenient way to identify and handle missing data in the 'Age' column. It helps in systematically managing and analyzing missing values in your dataset, and you can use it in various data analysis or machine learning tasks as needed.

# In[16]:


dataframe.head()


# In[ ]:




