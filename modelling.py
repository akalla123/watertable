
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np

train = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\train_values_new.csv")

test = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\test_values_new.csv")

features = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\features_new.csv")


# In[26]:


train.head()


# In[27]:


testlist = list(test)
for i in range(0,len(testlist)):
    a = str(testlist[i])
    test[a] = test[a].astype(float)
    train[a] = train[a].astype(float)


# In[28]:


test.head()


# In[29]:


from sklearn import preprocessing
x = train.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
train = pd.DataFrame(x_scaled)
train.head()


# In[30]:


from sklearn import preprocessing
y = test.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
y_scaled = min_max_scaler.fit_transform(y)
test = pd.DataFrame(y_scaled)
test.head()


# In[31]:


train.head()


# In[32]:


train.to_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\train1111.csv", index = None)


# In[58]:


features = pd.DataFrame(features['status_group'])


# In[59]:


features.head()


# In[85]:


from sklearn.neighbors import KNeighborsClassifier

clf =  KNeighborsClassifier(n_neighbors=3)
clf.fit(train, features)


# In[86]:


a = clf.predict(test)
a.shape


# In[87]:


features1 = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\test_values.csv")


# In[88]:


result = pd.DataFrame(features1['id'])


# In[89]:


result['status_group'] = a


# In[90]:


result.head()


# In[91]:


result.to_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\result3.csv", index = None)

