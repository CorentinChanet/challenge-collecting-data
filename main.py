import time
import random
from utils.output import raw_to_csv, clean_to_csv, cleaning, _threads_to_dict
from utils.fetching import fetching_urls, fetching_data, FetchThread
from selenium import webdriver
from threading import Thread
from bs4 import BeautifulSoup
import requests
import json

threads = list()

def main():

    driver_name = input("Select webdriver: safari, chrome or firefox")

    i=1
    while i<3:
        url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={i}&orderBy=newest"
        urls = fetching_urls(url, driver_name)
        t = FetchThread(name='Test_{}'.format(i), target=fetching_data, args=(urls,))
        t.start() # fetching_data(urls)
        threads.append(t)
        time.sleep(0.5 + random.random())
        i += 1

    print(_threads_to_dict(threads))

    #raw_to_csv()

    #cleaning()

    #clean_to_csv()

    #driver.close()

    pass


if __name__ == '__main__':
    main()