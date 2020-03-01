#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[5]:


X= np.array([[1,2],[3,4]])
X


# In[9]:


v= np.array([1,2]).reshape([2,1])


# In[7]:


v


# In[15]:


v= np.array([1,2])
v


# In[16]:


np.dot(X,v)


# In[12]:


X*v


# In[13]:


np.dot(v,X)


# In[14]:


X-X.mean(axis=0)


# In[17]:


X.mean()


# In[18]:


import scipy
import scipy.linalg
scipy.linalg.svd(X, full_matrices=False)


# In[19]:


import matplotlib.pyplot as plt
#%matplotlib qt
x= np.linspace(0,10,50)


# In[20]:


x


# In[21]:


sinus = np.sin(x)


# In[22]:


plt.plot(x, sinus)
plt.show()


# In[ ]:




