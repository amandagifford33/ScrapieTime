import requests
from BeautifulSoup import BeautifulSoup 

url = 'https://www.indeed.com/jobs?q=Entry-Level+Machine+Learning+&l=San+Francisco&radius=25'
response = requests.get(url)
html = response.content


soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})
print soup.prettify()
