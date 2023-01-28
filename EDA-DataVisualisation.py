#!/usr/bin/env python
# coding: utf-8

#  ## line plot

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


fmri=sns.load_dataset("fmri")


# In[3]:


fmri.head()


# line plot with time and signal column data

# In[4]:


sns.lineplot(x="timepoint",y="signal",data=fmri)
plt.show()


# In[5]:


sns.lineplot(x="timepoint",y="signal",data=fmri,hue="event")
plt.show()


# adding markers for value point

# In[6]:


sns.lineplot(x="timepoint",y="signal",data=fmri,hue="event",style="event",markers=True)
plt.show()


#  ## barplot

# In[7]:


import pandas as pd
pokemon=pd.read_csv('pokemon.csv')


# In[8]:


pokemon.head()


# checking speed of legendary pokemon

# In[9]:


sns.barplot(x="is_legendary",y="speed",data=pokemon)
plt.show()


# checking weight of legendary pokemon

# In[10]:


sns.barplot(x="is_legendary",y="weight_kg",data=pokemon)
plt.show()


# adding a hue to show pokemon generation

# In[11]:


sns.barplot(x="is_legendary",y="speed",hue="generation",data=pokemon)
plt.show()


# using palettes to assign different color elements

# In[12]:


sns.barplot(x="is_legendary",y="speed",palette="vlag",data=pokemon)
plt.show()


#  ## scatter plot

# In[13]:


iris=pd.read_csv("IRIS.csv")


# In[14]:


iris.head()


# In[17]:


sns.scatterplot(x="sepal_length",y="petal_length",data=iris)
plt.show()


# In[18]:


sns.scatterplot(x="sepal_length",y="petal_length",data=iris,hue="species")
plt.show()


# adding heu on petal length to differentiate

# In[20]:


sns.scatterplot(x="sepal_length",y="petal_length",data=iris,hue="petal_length")
plt.show()


#  ## histogram/dist plot

# In[22]:


diamonds=pd.read_csv('diamonds.csv')


# In[23]:


diamonds.head()


# In[24]:


sns.distplot(diamonds['price'])
plt.show()


# printing only frequency curve

# In[26]:


sns.distplot(diamonds['price'],hist=False)
plt.show()


# In[27]:


sns.distplot(diamonds['price'],bins=5)
plt.show()


# on vertical axis

# In[29]:


sns.distplot(diamonds['price'],bins=5,vertical=True)
plt.show()


# In[ ]:




