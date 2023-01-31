#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import pandas as pd
import numpy as np


# In[2]:


from App import Recommender


# In[6]:


class RecommenderDS():

    def __init__(self):
        pass

    def deserialize(self):
        # Deserializing
        with open('movie.pkl', 'rb') as handle:
            model = pickle.load(handle)
        return model

    def recommendation(self, title):
        model = self.deserialize()
        return model.get_recommendation(title)


# In[ ]:


# In[ ]:


# In[ ]:
a = 2
if (a == 2):
print("hello")

print(ok)
