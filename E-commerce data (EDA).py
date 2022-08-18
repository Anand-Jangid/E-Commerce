#!/usr/bin/env python
# coding: utf-8

# # Importing essential libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


file_path='D:\data\FashionDataset.csv'
data=pd.read_csv(file_path)


# # Reading file

# In[3]:


data.head()


# In[4]:


data.info()


# # Converting  MRP column

# In[5]:


data["MRP"]=data['MRP'].apply(lambda x: x[4:])


# In[6]:


data.head()


# In[7]:


data["MRP"].unique()


# In[8]:


data.loc[data['MRP']=='','MRP']='0'


# ## Converting MRP datatype to integer value

# In[9]:


data['MRP']=data['MRP'].astype('int64')


# In[10]:


data['MRP'].dtypes


# ## Replacing 0 with mean value

# In[11]:


mean_value=data[~(data['MRP']==0)]['MRP'].mean()


# In[12]:


mean_value


# In[13]:


data.loc[data['MRP']==0,'MRP']=mean_value


# In[14]:


data[data['MRP']==0]


# ## 0 values has been replaced

# In[15]:


data.head()


# In[16]:


data['Discount'].unique()


# ## Replacing Nan in 'Discount' coulmn to 0% off

# In[17]:


data.loc[data['Discount']=='Nan','Discount']='0% off'


# In[18]:


data['Discount'].unique()


# In[19]:


data['Disc']=data['Discount'].apply(lambda x: x[:-5])


# In[20]:


data.head()


# In[21]:


data['Disc']=data["Disc"].astype("int64")


# In[22]:


data.shape


# ## Converting SellPrice column

# In[23]:


data[data['SellPrice']=="Nan"]['Sell']


# In[24]:


data=data[data['SellPrice']!='Nan']


# In[25]:


data.shape


# In[26]:


data['SellPrice'].unique()


# In[27]:


data['SellPrice']=data['SellPrice'].astype('int64')


# In[28]:


data.SellPrice.dtype


# ## Crearting Profit Column

# In[29]:


data['Profit']=data['SellPrice']*(1-(data["Disc"]/100))-data['MRP']


# In[30]:


data.head()


# In[32]:


data['BrandName'].unique()


# ## understanding the data

# In[34]:


data.groupby('BrandName')['MRP','SellPrice','Profit'].max()


# In[35]:


data.head()


# In[36]:


data.Category.unique()


# In[42]:


db=data.groupby('Category')['MRP','SellPrice','Profit'].mean()
print(db.round(2))


# In[49]:


plt.plot(db['MRP'],'r',label='MRP')
plt.plot(db['SellPrice'],'g',label="SellPrice")
plt.plot(db['Profit'],'b',label='Profit')
plt.grid()
plt.show()


# In[ ]:




