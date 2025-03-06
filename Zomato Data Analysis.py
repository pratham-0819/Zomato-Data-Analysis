#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


dataframe=pd.read_csv(r"C:\Users\Prathmesh\Downloads\Zomato-data-.csv")
print(dataframe.head())


# In[7]:


#to convert rating!(data cleaning)
def rate(value):
    value=str(value).split('/')#splits the rating and stores into list.
    value=value[0];#selects data at index '0' in list.
    return float(value)

dataframe['rate']=dataframe['rate'].apply(rate)
print(dataframe.head())


# In[8]:


dataframe.info()


# In[11]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# In[20]:


group_data= dataframe.groupby('listed_in(type)')['votes'].sum()
result= pd.DataFrame({'votes':group_data})
plt.plot(result,c='green',marker='o')
plt.xlabel("type of restaurant",c='red',size=18)
plt.ylabel("votes",c='red',size=18)


# In[26]:


max_votes=dataframe['votes'].max()
reastaurant_with_max_votes=dataframe.loc[dataframe['votes']== max_votes,'name']

print("reastaurant_with_max_votes")
print(reastaurant_with_max_votes)


# In[28]:


sns.countplot(x=dataframe['online_order'])


# In[30]:


plt.hist(dataframe['rate'])
plt.title("rating distribution")


# In[36]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.title('approx_cost')


# In[38]:


sns.boxplot(x='online_order',y='rate',data=dataframe)
plt.title("online vs offline ratio")


# In[ ]:




