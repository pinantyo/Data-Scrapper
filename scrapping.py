# import twint


# list_tweet = ["#Jokowi","#GelorakanGanjarPranowo","Layani Korban Bencana","#TolakRUUOmnibuslaw_Kesehatan","#barugajian","#HadirkanSenyuman","#BennyRhamdaniBapakPMI"]

# for i in list_tweet:
# 	c = twint.Config()

# 	c.Search = [i]       # topic
# 	c.Limit = 500      # number of Tweets to scrape
# 	c.Store_csv = True       # store tweets in a csv file
# 	c.Output = f"data/{i}.csv"     # path to csv file

# 	twint.run.Search(c)


# Detik.com
from bs4 import BeautifulSoup
import requests


url = str(input('Input URL'))
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
# div_content = soup.find_all("div", {"class": "detail__body-text itp_bodycontent"})
div_content = soup.select("div.detail__body-text.itp_bodycontent")
print(div_content[0].get_text().strip())