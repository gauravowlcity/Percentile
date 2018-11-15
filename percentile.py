
# coding: utf-8

# In[7]:


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
# path 
# Importing the dataset
df = pd.read_csv('data_percentile.csv')
pd.options.display.float_format = '{:20,.6f}'.format


# In[8]:


df.head()


# In[10]:


percentile=df['month_count'].quantile([.25, .75])
print(percentile)


# In[17]:


x=percentile[.25]
y=percentile[.75]


# In[30]:


sub=df[(df['month_count']>=x) & (df['month_count']<=y)]
sub.groupby('account_rank')['month_count'].max()


# In[33]:


sub.groupby('account_rank').agg({'month_count':['median','mean','max','min'],'account_num':['count']})

