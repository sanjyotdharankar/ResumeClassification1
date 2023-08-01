#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nltk')


# In[2]:


get_ipython().system('pip install spacy')


# In[4]:


get_ipython().system('pip install textract')


# In[28]:


import os
import re
import nltk
import spacy
import string
import pandas as pd
import textract
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[9]:


os.listdir('Resumes/Resumes')


# In[12]:


file_path1=[]
category1=[]
dir1='Resumes/Resumes/Peoplesoft resumes/'
for i in os.listdir(dir1):
    if i.endswith('.docx'):
        os.path.join(dir1,i)
        file_path1.append((textract.process(os.path.join(dir1,i))).decode('utf-8'))
        category1.append('PeopleSoft')


# In[13]:


data1=pd.DataFrame(data=file_path1,columns=['Raw'])
data1['Category1']=category1
data1


# In[14]:


file_path2=[]
category2=[]
dir2='Resumes/Resumes/React/'
for i in os.listdir(dir2):
    if i.endswith('.docx'):
        os.path.join(dir2,i)
        file_path2.append((textract.process(os.path.join(dir2,i))).decode('utf-8'))
        category2.append('React')


# In[15]:


data2=pd.DataFrame(data=file_path2,columns=['Raw'])
data2['Category2']=category2
data2


# In[16]:


file_path3=[]
category3=[]
dir3='Resumes/Resumes/SQL Developer Lightning insight/'
for i in os.listdir(dir3):
    if i.endswith('.docx'):
        os.path.join(dir3,i)
        file_path3.append((textract.process(os.path.join(dir3,i))).decode('utf-8'))
        category3.append('SQL')


# In[17]:


data3=pd.DataFrame(data=file_path3,columns=['Raw'])
data3['Category3']=category3
data3


# In[20]:


file_path4=[]
category4=[]
dir4='Resumes/Resumes/workday resumes/'
for i in os.listdir(dir4):
    if i.endswith('.docx'):
        os.path.join(dir4,i)
        file_path4.append((textract.process(os.path.join(dir4,i))).decode('utf-8'))
        category4.append('workday r')


# In[21]:


data4=pd.DataFrame(data=file_path4,columns=['Raw'])
data4['Category4']=category4
data4


# In[29]:


df=data1.append([data2,data3,data4])
df


# In[30]:


df.info()


# In[32]:


df.duplicated().sum()


# In[35]:


df['Category']=category1+category2+category3+category4
df


# In[37]:


df.drop(['Category1','Category2','Category3','Category4'],axis=1,inplace=True)
df


# In[39]:


df.to_csv('Resume.csv',index=False)


# In[ ]:




