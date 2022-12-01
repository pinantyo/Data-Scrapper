import requests, io
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader



URL = "https://garuda.kemdikbud.go.id/journal"


def info(pdf_path):
	response = requests.get(pdf_path)

	with io.BytesIO(response.content) as f:
		pdf = PdfFileReader(f)

		information = pdf.getDocumentInfo()
		num_pages = pdf.getNumPages()

	txt = f"""
	Information about {pdf_path}

	Author: {information.author}
	Creator: {information.creator}
	Producer: {information.producer}
	Subject: {information.subject}
	Title: {information.title}
	Number of pages: {num_pages}
	"""

	print(txt)

	return information




if __name__ == "__main__":
	request = requests.get(URL)
	html_content = read.content
	soup = BeautifulSoup(html_content, "html.parser")

	# Init set
	list_pdf = set()
	l = soup.find('p')
	p = l.find_all('a')

	for link in p:
		print(f'Links: {link.get("href")}', end="\n")
		pdf_link = (link.get('href')[:-5]) + ".pdf"
		list_pdf.add(pdf_link)

	for i in list_pdf:
		info(i)


	print('Scrapping Finished')
