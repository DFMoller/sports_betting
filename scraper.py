from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
from comm import addSearches, getSearches, postReadings, postHistory, deleteOldEntries


current_url = "www.google.com"
html_text = requests.get(current_url).text
soup = BeautifulSoup(html_text, 'lxml')
search_results = soup.find_all('div', class_='e-available m-has-photos')
page_numbers = soup.find('div', class_='b-pagination-bar').find('div', class_='gm-show-inline-block').findChildren()
pages = int(page_numbers[-1].text) # finds last item in list