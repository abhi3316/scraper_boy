import requests 
from bs4 import BeautifulSoup


#news_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="
#speech_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=speeches&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

#statement_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=statements&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

#background_url = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=backgrounders&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="

#media_advisories = "https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=mediaadvisories&dprtmnt=departmentofcitizenshipandimmigration&start=2015-01-01&end="


def news_get(url):
	#url = background_url

	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')

	news = soup.find('div', class_= "mwsharvest section")
	news_article = news.find_all('article')

	count = 0;
	for at in news_article:
		par = at.find_all('p')
		for par_s in par:
			print("[{}]. {}".format(count, par_s.get_text(strip = True)))
		#print(par[1].get_text(strip=True))
