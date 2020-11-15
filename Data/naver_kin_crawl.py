#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
import requests
import random
from random import randint
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException


# In[ ]:


# creating a list of dates from which to crawl data
date = []

for i in ["201912","202001","202002","202003", "202004"] :
    for j in range(1,32) :
        temp = ""
        if len(str(j)) == 1 :
            temp = "0" + str(j)
        elif i == "202002" and j > 29 :
            continue
        elif i == "202003" and j > 31 :
            continue
        elif i == "202004" and j > 20 :
            continue
        else :
            temp = str(j)
        date.append(i+temp)


# In[ ]:


# retrieving Q&A post URLs as a list from search result (by date)

urls = []
driver = webdriver.Chrome('/Users/SeoyeonHong/Downloads/chromedriver')
for k in date[90:]:
    i = 1
    while i <= 100:
        driver.get("https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Afrom{}to{}&query=%EC%BD%94%EB%A1%9C%EB%82%98+%EA%B0%80%EB%8A%A5%ED%95%9C%EA%B0%80%EC%9A%94&c_id=&c_name=&sm=tab_pge&kin_start={}".format (k, k, (i-1)*10 + 1))
        time.sleep(random.uniform(1,1.5))
        html = driver.page_source
        soup = bs(html, 'html.parser')
        questions = soup.select("dt.question")
        for question in questions[:]:
            url = question.find("a")["href"]
            urls.append(url)
        i = i + 1
driver.close()


# In[ ]:


driver = webdriver.Chrome('/Users/SeoyeonHong/Downloads/chromedriver')


# In[ ]:


date = []
q_title = []
q_content = []


# In[ ]:


def naver_kin_crawler(url):
    driver.get(url)
    time.sleep(random.uniform(1,1.2))
    html = driver.page_source
    soup = bs(html, "html.parser")
    # post date
    date_ = soup.find('span', {'class':'c-userinfo__info'}).get_text().strip('작성일')
    date.append(date_)
    # question title
    q_title_elem = soup.select("div.c-heading__title")[0]
    q_title_ = q_title_elem.get_text().strip()
    q_title_ = q_title_.replace("\n", "")
    q_title_ = q_title_.replace("\t", "")
    q_title.append(q_title_)
    # question
    try:
        q_content_ = q_title_elem.find_next_sibling('div').get_text().strip()
    except AttributeError:
        q_content_ = " "
    q_content_ = q_content_.replace("\xa0", " ")
    q_content.append(q_content_)


# In[ ]:


for url in urls[:]:
    naver_kin_crawler(url)


# In[ ]:


data_ = zip(date, q_title, n_q_content)
df = pd.DataFrame(data = data_, columns=["date", "q_title", "q_content"])


# In[ ]:


df.to_csv("/Users/SeoyeonHong/Desktop/text_mining/covid_kin.csv")


# In[ ]:


driver.close()

