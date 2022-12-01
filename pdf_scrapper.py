import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfReader
import os

def get_data(pdf_path):
	text_pdf = []

	with open(pdf_path, 'rb') as f:
		pdf = PdfReader(f)
		information = pdf.getDocumentInfo()
		number_of_pages = pdf.getNumPages()

		for i in range(number_of_pages):
			page_content = pdf.getPage(i)
			print(page_content.extract_text())
			text_pdf.append(page_content.extract_text())

	txt = f"""
	Information about {pdf_path}:

	Author: {information.author}
	Creator: {information.creator}
	Producer: {information.producer}
	Subject: {information.subject}
	Title: {information.title}
	Number of pages: {number_of_pages}
	"""
	print(f'Info scrapping: {txt}')


	print("Scrapped Data")	

	return " [PAGE_BREAK] ".join(text_pdf)



def download_pdf(url, file_name, headers):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(f'pdf/{file_name}', "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


if __name__ == '__main__':

	# Init URL
	url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"


	# Create dir
	if os.path.exists('pdf') == False:
		os.mkdir('pdf')


	# Get Web
	read = requests.get(url)
	
	# Get HTML Content
	html_content = read.content
	soup = BeautifulSoup(html_content, "html.parser")

	# Get PDF Link
	l = soup.find('div', {'class','text'})
	links = l.find_all('a')

	# Init Header
	headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }


    # Download each link
	for index, link in enumerate(links):
		pdf_link = link.get('href')

		# Gdrive
		if pdf_link[-7:] == 'sharing':
			pdf_link = f"https://drive.google.com/uc?id={pdf_link.split('/')[5]}"
		print(pdf_link)

		file_name = f"file{index+1}.pdf"
		download_pdf(pdf_link, file_name, headers)




	list_of_pds = [f'pdf/{i}' for i in os.listdir('pdf')]


	for i in list_of_pds:
		print(get_data(i))








