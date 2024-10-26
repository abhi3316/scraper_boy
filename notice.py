import requests
from bs4 import BeautifulSoup



RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"  # Reset to default color



# URL of the page to scrape
url = "https://www.canada.ca/en/immigration-refugees-citizenship/news/notices.html"

# Send a GET request to the URL
response = requests.get(url)

link = []
notice = []
# Check if the request was successful


if response.status_code == 200:
	soup = BeautifulSoup(response.content, 'html.parser')
	year = soup.find('h2', string='2024')

	# Get the next sibling (the <ul> tag) containing the list of notices
	if year:
		notices_list = year.find_next_sibling('ul')
	count = 0
	if notices_list:
		for li in notices_list.find_all('li'):
			print(li.get_text(strip=True))
			notice.append(li.get_text(strip=True))
			#str = "https://www.canada.ca/".format(li.find('a')['href'])
			link.append("https://www.canada.ca/{}".format(li.find('a')['href']))
	else:
		print("No 2015 section found.")




inp = int(input("Link:"))

print("{}Link is : {}{}".format(RED, link[inp], RESET)) # Warnings to be print in red

response = requests.get(link[inp])
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup)
target_div = soup.find('div', class_='mwsgeneric-base-html parbase section')

#print(target_div)

paragraph = target_div.find_all('p')
for p in paragraph:
	print(" {}".format(p.get_text(strip=True)))
	print("")
	# Extract and print all tables
	#tables = target_div.find_all('table')
	#for table in tables:
	#	print("Table:")
	#	for row in table.find_all('tr'):
	#		row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
	#		print("  ", row_data)


#for par in soup.find_all('p'):
#	content = par.get_text(strip = True)
#	print(content)
