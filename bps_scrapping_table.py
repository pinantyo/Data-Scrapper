import requests, os, io, random, re

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests import get

page = 1

DOMAIN = 'https://www.bps.go.id'
URL = [
	f'/indicator/13/633/{page}/posisi-kredit-investasi-perbankan-menurut-sektor-ekonomi-format-baru-.html',
	f'/indicator/13/634/{page}/posisi-kredit-modal-kerja-perbankan-menurut-sektor-ekonomi-format-baru-.html',
	'/indicator/13/284/1/kurs-tengah-beberapa-mata-uang-asing-terhadap-rupiah-di-bank-indonesia-dan-harga-emas-di-jakarta.html',
	'/indicator/13/1962/1/posisi-kredit-usaha-mikro-kecil-dan-menengah-umkm-sup-1-sup-pada-bank-umum-.html',
	'/indicator/13/125/1/transaksi-dan-indeks-saham-di-bursa-efek.html',
	'/indicator/1/379/1/bi-rate.html'
]

DIR_PATH = 'D:/Project/BNI/Scrapping/data/bps'

HEADERS = {
	"User-Agent": "Chrome/51.0.2704.103",
}

def extract_data_each_year(url_path, headers, file_name, year):

	files_dir = os.path.join(DIR_PATH, file_name)

	if not os.path.exists(files_dir):
		os.mkdir(files_dir)


	cols = ['keterangan']
	rows = []
	df = None



	html = requests.get(url_path, headers=headers)

	if html.status_code == 200:
		html = html.text

		soup = BeautifulSoup(html, "lxml")
		table = soup.find('table', id='tablex')

		cols += [i.text for i in table.find('thead').find_all('tr')[-1].find_all('th')]



		df = pd.DataFrame(columns=cols)



		bodies = soup.find_all('tbody')[0]

		for i in bodies.find_all('tr'):
			length = len(df)

			df.loc[length] = [j.text for j in i.find_all('td')]



	df.to_csv(os.path.join(files_dir, f'{file_name} {year}.csv'), index=False)

if __name__ == '__main__':
	for local_url in URL:
		html = requests.get(DOMAIN + local_url).text


		file_name = local_url.split('/')[-1].split('.')[0]


		if not os.path.exists(DIR_PATH):
			os.mkdir(DIR_PATH)


		soup = BeautifulSoup(html, "lxml")


		anchors = soup.find_all('select')
		if anchors:
			url_years = [i.get('value') for i in anchors[0].find_all('option')[1:]]

			year = [i.text for i in anchors[0].find_all('option')[1:]]

			for i, j in list(zip(url_years, year)):
				extract_data_each_year(DOMAIN+i, HEADERS, file_name, j)



		
		else:
			anchors = soup.find_all('ul', {'class':'yiiPager'})[0]
			anchors = anchors.find_all('li', {'class':'page'})

			for i in anchors:
				anchor = i.find('a')
				url_years = anchor.get('href')
				year = anchor.text

				extract_data_each_year(DOMAIN+url_years, HEADERS, file_name, year)