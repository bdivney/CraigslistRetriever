from bs4 import BeautifulSoup
import requests
import datetime

todayUNF = datetime.datetime.now()
month = todayUNF.strftime("%b")
dayNum = todayUNF.strftime("%d").strip("0")
todayF = "{}  {}".format(month, dayNum)

print("Enter an item you want to search for:")
searchTerm = input().replace(" ", "+")
page = requests.get("https://southbend.craigslist.org/search/sss?sort=date&query={}".format(searchTerm))

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('li')

print('-----------------------------------------')

for entry in data:
	listing = entry.find('a', class_="result-title hdrlnk")
	price = entry.find('span', class_="result-price")
	postDate = entry.find('time', class_="result-date")
	if listing and postDate.get_text() == todayF:
		print("{} : {} : {}".format(postDate.get_text(), listing.get_text(), price.get_text()))
		print('-----------------------------------------')
