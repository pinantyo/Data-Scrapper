import requests, os, io
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import pandas as pd

"""
	Algo:

	1. Request https://garuda.kemdikbud.go.id/area/index/60?page=1
	2. Ambil link a dengan class title-journal
	3. Request link tahap ke 2
	4. Ambil link a dengan class title-citation
	5. Request link tahap ke 4 (Untuk mengunduh PDF)
	6. Proses Extract Informasi dari Paper

"""

text_pdf = []



def normalize_text(text):
	email_pattern = re.compile(r'[\w._%+-]+@[\w\.-]+\.[a-zA-Z]{2,4}')
	phone_pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4,6}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4,6}|\d{3,4}[-\.\s]??\d{4,6})')
	url_pattern = re.compile(r'www|http:|https:+[^\s]+[\w]')

	text = re.sub(email_pattern, "", text)
	text = re.sub(phone_pattern, "", text)
	text = re.sub(url_pattern, "", text)

	text = text.lower()                                   # Mengubah teks menjadi lower case
	text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
	text = re.sub(r'https?://\S+|www\.\S+', "", text)     # Menghapus URL
	text = re.sub(r'[-+]?[0-9]+', "", text)               # Menghapus angka
	text = re.sub(r'[^\w\s,.]', "", text)                 # Menghapus karakter tanda baca

	text = text.split()
	text = [i.strip() for i in text]
	return " ".join(text)


def visitor_body(text, cm, tm, fontDict, fontSize):
	y = tm[5]
	if y > 50 and y < 720:
		text_pdf.append(text)


def get_data(pdf_path):
	global text_pdf
	text_pdf = []

	try:
		with open(pdf_path, 'rb') as f:
			pdf = PdfReader(f, strict=False)
			number_of_pages = pdf.getNumPages()
			for i in range(number_of_pages):
				page_content = pdf.getPage(i)
				page_content.extract_text(visitor_text=visitor_body)
	except:
		print(f'{pdf_path} can\'t be scrapped')

	else:	
		return " ".join(text_pdf)


if __name__ == '__main__':
	list_of_pds = [f'pdf/{i}' for i in os.listdir('pdf')]

	if not os.path.exists('scrapped_data'):
		os.mkdir('scrapped_data')

	for index, i in enumerate(list_of_pds):
		try:
			content = normalize_text(get_data(i))
		except:
			print(f'{i} can\'t be scrapped')
		else:
			if content:
				try:
					with open(f'scrapped_data/{index}.txt', 'w', encoding="utf-8") as f:
						f.write(content)
				except:
					print(f'{i} can\'t be scrapped')

		print(f"PDF {i} scrapped")


	print('Data Scrapped')


	# df = pd.DataFrame.from_dict(content)
	# df.to_csv('CSITScrapped.csv')