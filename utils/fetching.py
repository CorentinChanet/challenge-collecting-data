import time
import random
from selenium import webdriver
from threading import Thread
from bs4 import BeautifulSoup
import requests
import json

def select_driver(name) -> webdriver:
    '''
    This function starts the corresponding webdriver if an appropriate name has been given.
    If name is not recognized, webdriver.Firefox() is started as default
    :param name: string
    :return: selenium.webdriver
    '''
    if name.lower() == 'safari':
        return webdriver.Safari()
    elif name.lower() == 'chrome':
        return webdriver.Chrome()
    else:
        return webdriver.Firefox()

def fetching_urls(url: str, driver: webdriver) -> list:
    '''
    This function uses a webdriver to connect to the url, and fetches all the links from that page.
    If some element passes as a link but does not have a href attribute, a message is printed and
    the function continues iterating over the page source code.
    :param url: string
    :param driver: webdriver
    :return: list
    '''
    driver.get(url)

    urls = []
    container = driver.find_element_by_id("main-content")
    for li in container.find_elements_by_tag_name("a"):
        try:
            urls.append(str(li.get_attribute("href")))
        except:
            print("No href found - passing over element")
            continue

    return urls

def fetching_data(url:str) -> dict:
    '''
    This function fetches all the relevant information relative to a single property on its webpage.
    :param url: string
    :return: tuple
    '''

    item_url = url
    r = requests.get(item_url)
    time.sleep(0.2)

    _dict = {'subtype': None, 'bedroomCount': None,
             'netHabitableSurface': None, "fireplaceExists": None,
             'terraceSurface': None,
             'hasTerrace': None, 'hasGarden': None, 'gardenSurface': None,
             'hasSwimmingPool': None}

    fields = tuple(_dict.keys())

    item_soup = BeautifulSoup(r.content)
    #print(item_soup)
    item_script = item_soup.select('#container-main-content div script')
    # item_string is bs4.element.Tag
    item_string = str(item_script[0])
    # so we cut the useful part of it to get a JSON string
    item_JSON = item_string[64:-19]
    # converting string to a Python dictionary
    item_parse = json.loads(item_JSON)

    item_property = item_parse['property']

    item_price_all = item_parse['price']
    _dict['price'] = item_price_all['mainValue']
    _dict['type'] = item_property['type']
    _dict['postalCode'] = item_property['location']['postalCode']
    _dict['locality'] = item_property['location']['locality']

    _dict['kitchen'] = None
    _dict['condition'] = None
    _dict['facadeCount'] = None
    _dict['isFurnished'] = None

    for field in fields:
        try:
            _dict[field] = item_property[field]
        except:
            print(f"Unable to fetch the feature {field} from script")

    try:
        _dict['kitchen'] = item_property['kitchen']['type']

    except:
        pass

    try:
        _dict['isFurnished'] = item_property['sale']['isFurnished']
    except:
        pass

    try:
        _dict['condition'] = item_property['building']['condition']
    except:
        pass

    try:
        _dict['facadeCount'] = item_property['building']['facadeCount']
    except:
        pass

    return _dict


class FetchThread(Thread):
    '''
    This class defines a classic thread targetting a function. The only differences are:
    | 1) It relies on try statement so as not to break if the target function breaks
    | 2) It stores the returned values of the target function in a .data attribute
    '''
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