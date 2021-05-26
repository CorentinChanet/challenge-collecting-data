import os
import requests
from bs4 import BeautifulSoup
import re
import lxml
#import time

start_url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&orderBy=newest'
_r = requests.get(start_url)
print(_r.status_code)
#time.sleep(1)
soup = BeautifulSoup(_r.content, 'html5lib')
#print(soup)
all_links = soup.find_all('a', attrs={'class': "footer__item"})
print(all_links)
