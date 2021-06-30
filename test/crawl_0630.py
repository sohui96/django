#!/usr/bin/env python
# coding: utf-8

# > import requests
#     - requests 가 최신 버전
# 
# > import urllib 
#     - file 을 다운로드 할 때는 urllib를 사용
# 
# - update 가 될 때마다 데려올 것임

# In[16]:


import requests


# In[17]:


res = requests.get('https://sejong.korea.ac.kr/campuslife/facilities/dining/weeklymenu')


# In[19]:


from bs4 import BeautifulSoup as bs
soup = bs(res.text, 'html.parser')


# In[62]:


tags = soup.select('#sub_contents > div > .subArea > p > span > a')


# In[63]:


tags


# In[72]:


tag = tags[0]
contect = tag.text
print(contect)
link = tag['href']
print(link)


# In[ ]:


tag = tags[0]
contect = tag.text
print(contect)
link = tag['href']
print(link)


# In[74]:


filename = 'https://sejong.korea.ac.kr/' + link
filename


# In[75]:


import urllib.request
urllib.request.urlretrieve(filename, filename.split('/')[-1])


# In[79]:


img_list = []
img_list = urllib.request.urlretrieve(filename, filename.split('/')[-1])

