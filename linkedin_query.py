import requests
from bs4 import BeautifulSoup

urls = []
ctr = 0

#Loop through first 15 pages (10 per page, so count 15*10=150)
while ctr < 150:
  query = 'https://google.com/search?q=site:linkedin.com/in AND Pablo Riveroll+Schroder Investment Management Limited'+str(ctr)
  
  response = requests.get(query)
  soup = BeautifulSoup(response.text,'html.parser')
  for anchor in soup.find_all('a'):
    url = anchor["href"]
    if 'https://www.linkedin.com/' in url:
      url = url[7:url.find('&')]
      urls.append([url])
      print(url)
  ctr = ctr+10
