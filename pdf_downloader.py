import requests, os, io, random
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader




dir_path_default = ''



def get_journal(path, domain, index_journal, journal_page, SPage):
	# Journal
	read = requests.get(path)
	
	# Get HTML Content
	html_content = read.content
	soup = BeautifulSoup(html_content, "html.parser")

	# Get Articles Link

	article_links = soup.find_all('div',{'class':'article-item'})


	print('Childs Link:')

	for index, link in enumerate(article_links):
		pdf_link = link.find_all('a',{'class':'title-citation'})[1].get('href')

		try:
			# Gdrive
			if pdf_link[-7:] == 'sharing':
				pdf_link = f"https://drive.google.com/uc?id={pdf_link.split('/')[5]}"

			file_name = f"SPage{SPage}Journal{index_journal}Page{journal_page}File{index+1}.pdf"
			download_pdf(pdf_link, file_name, headers)

			print(pdf_link)

		except:
			print(f'Can\'t download {pdf_link}')


			


def download_pdf(url, file_name, headers):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(f'{dir_path_default}/{file_name}', "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)



if __name__ == '__main__':
	# Init URL
	domain = "https://garuda.kemdikbud.go.id"
	url = "/area/index/60"


	# Create dir
	if not os.path.exists('pdf'):
		os.mkdir('pdf')
		dir_path_default = 'pdf'
	else:
		random_int = random.randint(1, 20)
		while True:
			if not os.path.exists(f'pdf{random_int}'):
				os.mkdir(f'pdf{random_int}')
				dir_path_default = f'pdf{random_int}'
				break


	# Get Web
	for index_site_page in range(49, 60):
		print(f'Pages: {domain+url}?page={index_site_page}')
		read = requests.get(domain+url+f'?page={index_site_page}')
		
		# Get HTML Content
		html_content = read.content
		soup = BeautifulSoup(html_content, "html.parser")

		# Get PDF Link
		# l = soup.find('div', {'class','text'})
		links = soup.find_all('a', {'class':'title-journal'})

		# Init Header
		headers = {
	        "User-Agent": "Chrome/51.0.2704.103",
	    }

	    # Download each link
		for index, link in enumerate(links[1:]):
			pdf_link = domain+link.get('href')
			
			for page_number in range(1, 5):
				print(f'Journal Link: {pdf_link}?page={page_number}')

				get_journal(pdf_link + f'?page={page_number}', domain, index, page_number, index_site_page)


	print('PDF Downloaded')








