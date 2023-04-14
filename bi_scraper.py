import requests, io, re, os, random, time

from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import numpy as np


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



"""
	Account
"""
"""
	USERNAME = 
	PASSWORD = 
"""



URL = 'https://www.bi.go.id/id/statistik/ekonomi-keuangan/seki/Default.aspx'




def init():
	options = Options()

	# options.add_argument("--headless")
	options.add_argument("--incognito")

	options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'


	DRIVER_PATH = 'D:\\Programs\\Python-packages\\WebDriver\\FirefoxDriver\\geckodriver.exe'
	driver = webdriver.Firefox(
		executable_path=DRIVER_PATH,
		options=options
	)
	driver.get(URL)

	return driver




def authentication(driver):
	login = driver.find_element_by_xpath("//input").send_keys(USERNAME)
	password = driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
	submit = driver.find_element_by_xpath("//input[@value='login']").click()


def extract_data(page):
	soup = BeautifulSoup(page)

	links = []

	for i in soup.find_all('tbody')[0].find_all('tr')[1:]:
		try:
			data = i.find_all('td')[-1].find('a').get('href')
		except:
			continue
		else:
			links.append(data)

	links = pd.DataFrame({
		'excel_links':links
	})

	links.to_csv("D:\\Project\\BNI\\Scrapping\\data\\bi_data_excel.csv")





if __name__ == '__main__':
	driver = init()
	element = driver.find_element(By.ID, 'MSOZoneCell_WebPartWPQ3')

	element.location_once_scrolled_into_view

	time.sleep(6)

	element = WebDriverWait(driver,5000).until(EC.visibility_of_element_located(
		(By.XPATH, "/html/body/form/div[12]/div/div[3]/div[2]/div[4]/div/div[1]/div[2]/div[1]/div[1]/div/div/a"))
	)	


	driver.execute_script("arguments[0].click();", element)

	time.sleep(6)

	html = driver.page_source

	extract_data(html)


	


