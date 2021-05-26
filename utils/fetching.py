import time
import random
from selenium import webdriver

def fetching_urls():
    driver = webdriver.Safari()

    list_url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance"

    driver.get(list_url)
    time.sleep(2)

    container = driver.find_element_by_id("main-content")
    for li in container.find_elements_by_tag_name("a"):
        print(li.get_attribute("href"))


    driver.close()

def fetching_data():
    pass