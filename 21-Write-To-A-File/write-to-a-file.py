import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'lxml')
titles = soup.find_all('h3', class_="indicate-hover")
for title in titles:
    with open('nyt_titles.txt', 'a') as open_file:
        open_file.write(title.text)
        open_file.write("\n")