import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(response.content, 'html.parser')

for item in soup.find_all('a'):
    print(item.get('href'))

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

# Scrape the data
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(response.content, 'html.parser')

# Categorize the links
internal_links = []
external_links = []
section_links = []

for item in soup.find_all('a', href=True):
    href = item.get('href')
    if href.startswith('#'):
        section_links.append(href)
    elif href.startswith('http'):
        external_links.append(href)
    else:
        internal_links.append(href)

# Create a DataFrame to hold the data
data = {
    'Type': ['Internal Links', 'External Links', 'Section Links'],
    'Count': [len(internal_links), len(external_links), len(section_links)]
}

df = pd.DataFrame(data)

# Visualize the data
plt.figure(figsize=(10, 6))
plt.bar(df['Type'], df['Count'], color=['blue', 'green', 'red'])
plt.xlabel('Type of Link')
plt.ylabel('Count')
plt.title('Count of Different Types of Links on Wikipedia Main Page')
plt.show()
