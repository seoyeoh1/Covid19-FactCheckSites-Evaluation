#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import time
import re
import requests
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException


# In[ ]:


driver = webdriver.Chrome('/Users/SeoyeonHong/Downloads/chromedriver')
actions = ActionChains(driver)


# In[ ]:


def search_query(query):
    search_bar = driver.find_element_by_id("search_content")
    search_bar.click()
    search_bar.send_keys(query)
    actions.send_keys(Keys.RETURN).perform()

url = "http://ncov.mohw.go.kr/factBoardList.do"
driver.get(url)
search_query("[팩트체크-바이러스]")


# In[ ]:


# question
html = driver.page_source
soup = bs(html, "html.parser")
titles = soup.select(".fl_ttl")
questions = []

for title in titles:
    question = title.get_text()
    question = question.replace('[팩트체크-바이러스]','')
    question = question.strip()
    questions.append(question)

print(len(questions))

# answer
responses = soup.select("[style*='font-size: 15pt']")
responses = soup.select(".fa_s_descript")
answers = []

for response in responses:
    answer = response.get_text()
    answer = answer.strip()
    answer = answer.replace('\n','')
    answer = answer.replace('\xa0','')
    answers.append(answer)
    
print(len(answers))

t_or_f = ['F', 'F', 'F']
url = [url]*len(questions)


# In[ ]:


zipped = zip(url, questions, answers, t_or_f)


# In[ ]:


df_virus = pd.DataFrame(data = zipped, columns=["url", "questions", "answers", "tf"])


# In[ ]:


frames = [df_virus, df_diagnosis, df_medical]
df = pd.concat(frames)


# In[ ]:


df.to_csv("/Users/SeoyeonHong/Desktop/text_mining/covid_mohwgov_factcheck.csv")


# In[ ]:




