import time
import random
from selenium import webdriver
from threading import Thread

def fetching_urls(url: str, driver) -> list:

    driver.get(url)

    urls = []
    container = driver.find_element_by_id("main-content")
    for li in container.find_elements_by_tag_name("a"):
        urls.append(li.get_attribute("href"))

    return urls

def fetching_data(urls: list, driver:str) -> dict:
    pass

class FetchThread(Thread):
    def __init__(self, driver, urls):
        Thread.__init__(self)
        self.urls = urls
        self.data = []
        self.drivers = {"safari": webdriver.Safari(), "chrome": webdriver.Chrome(), "firefox": webdriver.Firefox()}
        self.driver = self.drivers[driver.lower()]

    def run(self):
        for url in self.urls:
            self.data.append(fetching_data(url))
            time.sleep(1+random.random())