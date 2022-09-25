#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

data = pd.read_csv('hw2.csv')


# In[69]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data = pd.read_csv('hw2.csv')

freq_table = pd.crosstab(data['subject_race'],'count_of_race', margins = True)

freq_table = freq_table / len(data)

# convert from decimals to % 
pd.options.display.float_format = '{:.2%}'.format

freq_table 


# In[72]:


df.plot(kind='bar', x = 'subject_race')


# In[39]:


freq_table = pd.crosstab(data['search_conducted'],'count_of_search_counducted')

freq_table = freq_table / len(data)

freq_table 


# In[ ]:





# In[86]:


data_crosstab = pd.crosstab(data['search_conducted'], data['subject_race'], normalize = 'index')


print(data_crosstab)


# In[84]:


data_crosstab = pd.crosstab(data['search_conducted'], data['subject_race'], normalize = 'columns')


print(data_crosstab)


# In[89]:


data_crosstab = pd.crosstab(data['search_conducted'], data['subject_race'])

data_crosstab = data_crosstab / len(data)

print(data_crosstab)


# In[ ]:





# In[ ]:




