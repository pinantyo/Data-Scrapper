import twint
import os
import tweepy

# list_tweet = ["@erickthohir AND @bni AND @bnicustomercare"]
# # user = ['CustomerCareBNI']

list_tweet = ['@bnicustomercare','@bnicustomercare AND @bni','@bnicustomercare OR @bni']
DIR = 'data'


if __name__ == '__main__':
	if not os.path.exists(DIR):
		os.mkdir(DIR)

	for i in list_tweet:
	# i = 'BNICustomerCare'
		c = twint.Config()
		# c.Username = "BNICustomerCare"
		c.Lang = "id"
		c.translate = True

		c.Search = i      			# topic
		c.Limit = 1000      				# number of Tweets to scrape
		c.Store_csv = True       		# store tweets in a csv file
		c.Output = f"data/{i}.csv"     	# path to csv file

		twint.run.Search(c)