import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(response.content, 'html.parser')

for item in soup.find_all('a'):
    print(item.get('href'))
