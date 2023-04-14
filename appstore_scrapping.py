import requests, os, re
import pandas as pd

from app_store_scraper import AppStore

import numpy as np


country = ['id', 'us']

for i in country:
	app = AppStore(country=i, app_name="bnidirect-mobile", app_id=1471093490)
	print(app.review(sleep=2000))

	df = pd.DataFrame(np.array(app.reviews),columns=['content'])

	df2 = df.join(pd.DataFrame(df.pop('content').tolist()))

	df2.to_csv(
		f'D:\\Project\\BNI\\Scrapping\\data\\Scrapped\\Appstore/playstorereview-BNIDirect-{i}.csv',
		encoding='utf-8-sig'
	)


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