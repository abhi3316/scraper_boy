import requests
from bs4 import BeautifulSoup 
import notice
import news
import signal
import os 

notice_url = "https://www.canada.ca/en/immigration-refugees-citizenship/news/notices.html"

news_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="
speech_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=speeches&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

statement_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=statements&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

background_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=backgrounders&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

media_advisories = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=mediaadvisories&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

year = 2024

def handle_sigterm(signum, frame):
    print("Received SIGTERM, shutting down gracefully.")
    # Perform cleanup here
    exit(0)


def main():
	print("Canada News Scrapping platform")
	signal.signal(signal.SIGTERM, handle_sigterm)
	try:
		while 1:
			print("1: News")
			print("2: Notice")
			inp = int(input("inp:"))
			if(inp == 1):
				print("1: News")
				print("2: Statement")
				print("3: Background")
				print("4: Media")
				print("5: Speech")
				news_inp = int(input("inp:"))
				if(news_inp == 1):
					news.news_get(news_url)
				if(news_inp == 2):
					news.news_get(statement_url)
				if(news_inp == 3):
					news.news_get(background_url)
				if(news_inp == 4):
					news.news_get(media_advisories)
				if(news_inp == 5):
					news.news_get(speech_url)
				else:
					print("Input wrong")	

			if(inp == 2):
				notice.notice_get(notice_url, year)
	except:
		print("\nClosing the program...")
		exit(0)

if __name__ == "__main__":
	main()
