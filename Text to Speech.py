#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[6]:


import pyttsx3
engine = pyttsx3.init()
speech=input("Say something: ")
engine.say(speech)
engine.runAndWait()


# In[ ]:




