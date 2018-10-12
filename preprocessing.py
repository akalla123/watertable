
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

train = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\train_values.csv")

test = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\test_values.csv")

features = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\features.csv")


# In[2]:


train = train.sort_values(by='id')
features = features.sort_values(by='id')
test = test.sort_values(by='id')


# In[3]:


train['funder'] = train['funder'].fillna(train['funder'].value_counts().idxmax())
train['installer'] = train['installer'].fillna(train['installer'].value_counts().idxmax())
train['subvillage'] = train['subvillage'].fillna(train['subvillage'].value_counts().idxmax())
train['public_meeting'] = train['public_meeting'].fillna(train['public_meeting'].value_counts().idxmax())
train['scheme_management'] = train['scheme_management'].fillna(train['scheme_management'].value_counts().idxmax())
train['scheme_name'] = train['scheme_name'].fillna(train['scheme_name'].value_counts().idxmax())
train['permit'] = train['permit'].fillna(train['permit'].value_counts().idxmax())


# In[4]:


train["date_recorded"] = train["date_recorded"].astype(str).str.split("-").str[0]
train.head()


# In[5]:


def outlier25(a):
    b = np.array(a)
    b = np.percentile(b, 25)
    return b
def outlier75(a):
    b = np.array(a)
    b = np.percentile(b, 75)
    return b


# In[8]:


def changeoutlier(y):
    IQR = outlier75(train[y]) - outlier25(train[y])
    train[y] = train.apply(lambda x: 100000000000 if x[y] > outlier75(train[y])+1.5*IQR or x[y] < outlier25(train[y])-1.5*IQR else x[y] ,axis=1)
#if train['Unnamed: 0'][i] > outlier75(train['Unnamed: 0'])+1.5*IQR or train['Unnamed: 0'][i] < outlier25(train['Unnamed: 0'])-1.5*IQR:
    #outlier_index0.append(i)
#print(outlier_index0)


# In[10]:


changeoutlier('amount_tsh')
train.head()


# In[11]:


train.head()


# In[198]:


def change(x):
    a = train[x].unique()
    a = list(a)
    train[x] = train.apply(lambda row: (a.index(row[x])),axis =1)


# In[199]:


change('amount_tsh')
change('funder')
change('date_recorded')
change('gps_height')
change('installer')
change('wpt_name')
change('num_private')


# In[200]:


change('basin')
change('subvillage')
change('region')
change('region_code')
change('district_code')
change('lga')
change('ward')


# In[201]:


change('population')
change('public_meeting')
change('recorded_by')
change('scheme_management')
change('scheme_name')
change('permit')
change('construction_year')
change('extraction_type')
change('extraction_type_group')
change('extraction_type_class')


# In[202]:


change('management')
change('management_group')
change('payment')
change('payment_type')
change('water_quality')
change('quality_group')
change('quantity')
change('quantity_group')
change('source')
change('source_type')


# In[203]:


change('source_class')
change('waterpoint_type')
change('waterpoint_type_group')


# In[204]:


train.head()


# In[205]:


test['funder'] = test['funder'].fillna(test['funder'].value_counts().idxmax())
test['installer'] = test['installer'].fillna(test['installer'].value_counts().idxmax())
test['subvillage'] = test['subvillage'].fillna(test['subvillage'].value_counts().idxmax())
test['public_meeting'] = test['public_meeting'].fillna(test['public_meeting'].value_counts().idxmax())
test['scheme_management'] = test['scheme_management'].fillna(test['scheme_management'].value_counts().idxmax())
test['scheme_name'] = test['scheme_name'].fillna(test['scheme_name'].value_counts().idxmax())
test['permit'] = test['permit'].fillna(test['permit'].value_counts().idxmax())


# In[206]:


test.columns[test.isna().any()].tolist()


# In[207]:


train1 = pd.read_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\train_values.csv")
train1 = train1.sort_values(by='id')
train1['funder'] = train1['funder'].fillna(train1['funder'].value_counts().idxmax())
train1['installer'] = train1['installer'].fillna(train1['installer'].value_counts().idxmax())
train1['subvillage'] = train1['subvillage'].fillna(train1['subvillage'].value_counts().idxmax())
train1['public_meeting'] = train1['public_meeting'].fillna(train1['public_meeting'].value_counts().idxmax())
train1['scheme_management'] = train1['scheme_management'].fillna(train1['scheme_management'].value_counts().idxmax())
train1['scheme_name'] = train1['scheme_name'].fillna(train1['scheme_name'].value_counts().idxmax())
train1['permit'] = train1['permit'].fillna(train1['permit'].value_counts().idxmax())


# In[208]:


test["date_recorded"] = test["date_recorded"].astype(str).str.split("-").str[0]


# In[209]:


def change1(y):
    a = train1[y].unique()
    a = list(a)
    test[y] = test.apply(lambda x: a.index(x[y]) if x[y] in a else 1000000,axis=1)   


# In[210]:


change1('amount_tsh')
change1('date_recorded')
change1('funder')
change1('gps_height')
change1('installer')
change1('wpt_name')
change1('num_private')


# In[211]:


change1('basin')
change1('subvillage')
change1('region')
change1('region_code')
change1('district_code')
change1('lga')
change1('ward')


# In[212]:


change1('population')
change1('public_meeting')
change1('recorded_by')
change1('scheme_management')
change1('scheme_name')
change1('permit')
change1('construction_year')
change1('extraction_type')
change1('extraction_type_group')
change1('extraction_type_class')


# In[213]:


change1('management')
change1('management_group')
change1('payment')
change1('payment_type')
change1('water_quality')
change1('quality_group')
change1('quantity')
change1('quantity_group')
change1('source')
change1('source_type')


# In[214]:


change1('source_class')
change1('waterpoint_type')
change1('waterpoint_type_group')


# In[215]:


test.head()


# In[216]:


test.head()


# In[188]:


train.to_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\train_values_new.csv",index=None)


# In[189]:


test.to_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\test_values_new.csv",index=None)


# In[217]:


features.to_csv("C:\\Users\\Ayush\\Desktop\\Data\\water\\features_new.csv",index=None)

