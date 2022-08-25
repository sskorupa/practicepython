import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'lxml')
titles = soup.find_all('p', class_="paywall")
for title in titles:
    print(title.text)

