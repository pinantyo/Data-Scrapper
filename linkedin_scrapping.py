from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd


PATH = input("Enter the Webdriver path: ")
USERNAME = input("Enter the username: ")
PASSWORD = input("Enter the password: ")

driver = webdriver.Chrome(PATH)


driver.get("https://www.linkedin.com/uas/login")
time.sleep(3)

email=driver.find_element_by_id("username")
email.send_keys(USERNAME)
password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)


def Scrape_func(a,b,c):
    name = a[28:-1]
    page = a
    time.sleep(10)

    driver.get(page + 'detail/recent-activity/shares/')  
    start=time.time()
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        end=time.time()
        if round(end-start)>20:
            break

    company_page = driver.page_source   

    linkedin_soup = bs(company_page.encode("utf-8"), "html")
    linkedin_soup.prettify()
    containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})
    print("Fetching data from account: "+ name)
    iterations = 0
    nos = int(input("Enter number of posts: "))
    for container in containers:

        try:
            text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper ember-view"})
            text = text_box.find("span",{"dir":"ltr"})
            b.append(text.text.strip())
            c.append(name)
            iterations += 1
            print(iterations)
            
            if(iterations==nos):
                break

        except:
            pass 

n = int(input("Enter the number of entries: "))
for i in range(n):
    post_links.append(input("Enter the link: "))
for j in range(n):
    Scrape_func(post_links[j],post_texts,post_names)

        
driver.quit()



URL = "https://www.linkedin.com/in/williamhgates"




"""
import requests, os, io, random, re

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests import get



URL = "https://www.linkedin.com/in/williamhgates"




html = requests.get(URL).text

print(html)

soup = BeautifulSoup(html, 'lxml')

experience = soup.find_all('section', {'class':'experience'})

print(experience)

experience = experience.find_all('ul', {'class':'experience__list'}).find_all('li', {'class':'experience-item'})

list_of_experience = {
	'name':None,
	'company':[],
	'years_of_exp':[],
	'positions':[]
}


list_of_experience['name'] = soup.find_all('h1', {'class':['top-card-layout__title','font-sans','text-lg','papabear:text-xl','font-bold','leading-open','text-color-text','mb-0']})

for i in experience:
	list_of_experience['company'].append(i.find('experience-group-header__company').text)
	list_of_experience['years_of_exp'].append(i.find('experience-group-header__duration').text)

	positions = i.find('experience-group__positions').find_all('li', {'class':'experience-group-position'})
	if len(positions) > 1:
		positions = []
		for j in positions:
			positions.append(j.find('profile-section-card__title').text)

	list_of_experience['positions'].append(positions)


print(list_of_experience)




"""
