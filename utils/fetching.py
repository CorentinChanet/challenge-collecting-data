import json
import os
import requests
from bs4 import BeautifulSoup
import re
import time
import random
from selenium import webdriver
from threading import Thread
from bs4 import BeautifulSoup
import requests
import json

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

def fetching_data(url:str):

    item_url = url
    r = requests.get(item_url)
    time.sleep(random.random())

    item_soup = BeautifulSoup(r.content)
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
    item_street = item_property['location']['street']
    item_street_number = item_property['location']['number']
    item_property_type = item_property['type']
    item_property_subtype = item_property['subtype']
    item_price = item_price_all['mainValue']
    #item_type_of_sale = [item_transcactions['subtype'],item_transcactions['lifeAnnuity']]
    item_number_of_rooms = item_property['bedroomCount']
    item_area = item_property['netHabitableSurface']

    print(f'\nPropery type and subtype is {item_property_type} {item_property_subtype}, located at {item_street} {item_street_number}, price is {item_price}, it has {item_number_of_rooms} rooms and {item_area} area')
    item_kitchen = item_property['kitchen']
    return item_property_type, item_property_subtype, item_price, item_number_of_rooms, item_area
    #item_kitchen = item_property['kitchen']
    #item_furnished
    #item_open_fire
    #item_terrace
    #item_garden
    #item_geo
    #item_facades
    #item_swimming_pool
    #item_situation


class FetchThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args)
        self.data = []
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        for arg in self._args:
            for url in arg:
                try:
                    self.data.append(self._target(url))
                except:
                    print("Failed to parse url: " + str(url))