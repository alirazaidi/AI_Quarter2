#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np
arr=np.arange(10).reshape(2,5)
arr


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[13]:


a=np.arange(10).reshape(2,5)

b=np.ones(10,np.int).reshape(2,5)
np.stack((a,b)).reshape(4,5)


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[22]:


a=np.arange(10).reshape(2,5)

b=np.ones(10,np.int).reshape(2,5)
np.hstack((a,b))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[26]:


a=np.arange(10).reshape(2,5)
a.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[30]:


a=np.arange(15).reshape(3,5)
a.flatten()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[32]:


a=np.arange(15)
a.reshape(3,5)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[35]:


arr1=np.arange(25).reshape(5,5)
np.square(arr1)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[37]:


arr1=np.arange(30).reshape(5,6)
np.mean(arr1)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[38]:


np.std(arr1)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[39]:


np.median(arr1)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[40]:


np.transpose(arr1)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[50]:


arr1=np.arange(16).reshape(4,4)
trace=np.trace(arr1)
trace


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[51]:


np.linalg.det(arr1)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[53]:


arr1=np.arange(16).reshape(4,4)
p5 = np.percentile(arr1, 5)
p5
p95 = np.percentile(arr1, 95)
p95


# ## Question:15

# ### How to find if a given array has any null values?

# In[56]:


arr1=np.arange(16).reshape(4,4)
np.isnan(arr1).any()

