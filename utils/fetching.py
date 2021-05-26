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