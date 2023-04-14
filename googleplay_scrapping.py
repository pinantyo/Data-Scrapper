import requests, os, re

import pandas as pd
import numpy as np

from google_play_scraper import app, Sort, reviews_all


lang = ['id','en']
country = ['id','us']

for i, j in list(zip(lang, country)):
	reviews = reviews_all(
	    'id.co.bni.bnidirectmobile',
	    sleep_milliseconds=0, # defaults to 0
	    lang=i, # defaults to 'en'
	    country=j, # defaults to 'us'  
	    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
	)

	df = pd.DataFrame(np.array(reviews),columns=['review'])

	df = df.join(pd.DataFrame(df.pop('review').tolist()))

	df.to_csv(f'D:\\Project\\BNI\\Scrapping\\data\\Scrapped\\Google Play/googleplayreview-BNIDirect-{i}-{j}.csv', encoding='utf-8-sig')
































# # from selenium.webdriver.support.ui import WebDriverWait as wait
# # from selenium import webdriver
# # def open_browser():
# #     driver = webdriver.Chrome("/home/felipe/Downloads/chromedriver")
# #     driver.get(url)
# #     driver.find_element_by_id('bt_gerar_cpf').click()
# #     text_field = driver.find_element_by_id('texto_cpf')
# #     text = wait(driver, 10).until(lambda driver: not text_field.text == 'Gerando...' and text_field.text)
# #     return text

# # print(open_browser())


# """
# 	Catatan:
# 	Reviews berada pada modal yang tidak ditampilkan
# """


# def normalize_text(text):
# 	email_pattern = re.compile(r'[\w._%+-]+@[\w\.-]+\.[a-zA-Z]{2,4}')
# 	phone_pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4,6}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4,6}|\d{3,4}[-\.\s]??\d{4,6})')
# 	url_pattern = re.compile(r'www|http:|https:+[^\s]+[\w]')

# 	text = re.sub(email_pattern, "", text)
# 	text = re.sub(phone_pattern, "", text)
# 	text = re.sub(url_pattern, "", text)

# 	text = text.lower()                                   # Mengubah teks menjadi lower case
# 	# text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
# 	text = re.sub(r'https?://\S+|www\.\S+', "", text)     # Menghapus URL
# 	text = re.sub(r'[-+]?[0-9]+', "", text)               # Menghapus angka
# 	text = re.sub(r'[^\w\s,.]', "", text)                 # Menghapus karakter tanda baca

# 	text = text.split()
# 	text = [i.strip() for i in text if len(i.strip()) > 1]
# 	return " ".join(text)

# 	"""
# 	1. Trigger: <div jsaction="JIbuQc:trigger.hdtuG">
# 	class VfPpkd-wzTsW
# 	"""

# if __name__ == '__main__':
# 	# Init List
# 	text_list = []

# 	# Init URL
# 	# Google Play
# 	domain = "https://play.google.com/store/"
# 	# url = "apps/details?id=src.com.bni&hl=id&gl=US"
# 	url = 'https://play.google.com/store/apps/details?id=src.com.bni&hl=id&gl=US'



# 	# browser = Browser()
# 	# browser.visit(domain+url)
# 	# button = browser.find_by_name('button1')
# 	# button.click()

# 	# Create dir
# 	if not os.path.exists('data'):
# 		os.mkdir('data')

# 	# Get Web
# 	read = requests.get(url)
	
# 	# Get HTML Content
# 	html_content = read.content
# 	soup = BeautifulSoup(html_content, "html.parser")


# 	# button = soup.find_all('button', {'class':'VfPpkd-LgbsSe'})[-1]

# 	# driver = webdriver.Chrome()
# 	# driver.get(url)
# 	# driver.find_element_by_class_name('VfPpkd-LgbsSe').click()

# 	"""
# 		1. Get class EGFGHd
# 		2. Get class h3YV2d Text
# 	"""
	
# 	"""

# 	comments = soup.find_all('div', {'class':'RHo1pe'})

# 	# Init Header
# 	headers = {
#         "User-Agent": "Chrome/51.0.2704.103",
#     }

#     # Download each link
# 	for index, comment in enumerate(comments):
# 		text = comment.find_all('div', {'class':'h3YV2d'})[0].getText()
# 		text_list.append(normalize_text(text))
# 	"""

# 	comments = soup.find_all('div', {'class','h3YV2d'})

# 	text_list = [i.getText() for i in comments]


# 	df = pd.DataFrame({
# 		'text':text_list
# 	})


			
# 			