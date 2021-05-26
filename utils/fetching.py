import json
import os
import requests
from bs4 import BeautifulSoup
import re
import time
import random
from selenium import webdriver
from threading import Thread

def select_driver(name):
    if name.lower() == 'safari':
        return webdriver.Safari()
    elif name.lower() == 'chrome':
        return webdriver.Chrome()
    else:
        return webdriver.Firefox()

def fetching_urls(url: str, driver_name) -> list:
    driver = select_driver(driver_name)
    driver.get(url)

    urls = []
    container = driver.find_element_by_id("main-content")
    for li in container.find_elements_by_tag_name("a"):
        try:
            urls.append(str(li.get_attribute("href")))
        except:
            print("No href found - passing over element")
            continue

    driver.close()

    return urls

def fetching_data(urls:list):
    driver = webdriver.Safari()
    for url in urls:
        driver.get(url)

        item_url = 'https://www.immoweb.be/en/classified/house/for-sale/uccle/1180/9310971?searchId=60acaf3b768b5'
        r = requests.get(item_url)
        print(item_url, r.status_code)
        item_soup = BeautifulSoup(r.content,'html5lib')
        #print(item_soup)
        item_script = item_soup.select('#container-main-content div script')
        # item_string is bs4.element.Tag
        item_string = str(item_script[0])
        # so we cut the useful part of it to get a JSON string
        item_JSON = item_string[64:-19]
        # converting string to a Python dictionary
        item_parse = json.loads(item_JSON)
        #print(item_parse)
        item_id = item_parse['id']
        item_seller = item_parse['customers']
        item_property = item_parse['property']
        item_price_all = item_parse['price']
        #item_transcactions = item_parse['transactions']

        item_adress = item_property['location']['street'] + item_property['location']['number']
        item_property_type = item_property['type']
        item_property_subtype = item_property['subtype']
        item_price = item_price_all['mainValue']
        #item_type_of_sale = [item_transcactions['subtype'],item_transcactions['lifeAnnuity']]
        item_number_of_rooms = item_property['bedroomCount']
        item_area = item_property['netHabitableSurface']

        print(item_property_type, item_property_subtype, item_price, item_number_of_rooms, item_area)
        #item_kitchen = item_property['kitchen']
        #item_furnished
        #item_open_fire
        #item_terrace
        #item_garden
        #item_geo
        #item_facades
        #item_swimming_pool
        #item_situation
        time.sleep(2)
        print("DATA FETCHED! : " + str(url))
        driver.close()



# class FetchThread(Thread):
#     def __init__(self, driver, urls):
#         Thread.__init__(self)
#         self.urls = urls
#         self.data = []
#         self.driver = driver
#
#     def run(self):
#         for url in self.urls:
#             # code to fetch data from script
#             print('THREAD STARTED')
#             time.sleep(1+random.random())
#
#         self.driver.close()