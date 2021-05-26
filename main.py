import time
import random
from utils.output import raw_to_csv, clean_to_csv, cleaning
from utils.fetching import fetching_data, fetching_urls
from selenium import webdriver
from threading import Thread


def main():
    driver = webdriver.Safari()

    i=1
    while True:
        url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={i}&orderBy=newest"
        urls = fetching_urls(url, driver)
        time.sleep(0.5 + random.random())


    fetching_data()

    raw_to_csv()

    cleaning()

    clean_to_csv()

    driver.close()

    pass


if __name__ == '__main__':
    main()