import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_web_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print('Failed to retrieve the webpage')
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_data(soup):
    data = []
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h1').text()
        link = article.find('h3').text()
        data.append({'title': title, 'link': link})
    return data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def main():
    url = 'https://paltech-weather02.netlify.app/'
    html_content = fetch_web_page(url)
    if html_content:
        soup = parse_html(html_content)
        data = extract_data(soup)
        save_to_csv(data, 'scraped_data.csv')
        print('Data saved to scraped_data.csv')

if __name__ == '__main__':
    main()
