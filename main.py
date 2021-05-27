import time
from utils.csv_converter import raw_to_csv, clean_to_csv
import random
from utils.fetching import fetching_urls, fetching_data, FetchThread, select_driver
from selenium import webdriver
from threading import Thread
from bs4 import BeautifulSoup
import requests
import json

threads = list()

def main():
    # Let the user chose the appropriate browser
    driver_name = input("Select webdriver: safari, chrome or firefox")
    driver = select_driver(driver_name)

    start = time.time()

    # Checks for both houses and apartments
    for property_type in ("house", "apartment"):
        i=1
        while i<300:
            url = f"https://www.immoweb.be/en/search/{property_type}/for-sale?countries=BE&page={i}&orderBy=newest"
            # Fetches a batch of url from the i-th search results page
            urls = fetching_urls(url, driver)
            # Initialize and starts a thread to fetch data from urls
            t = FetchThread(name='Test_{}'.format(i), target=fetching_data, args=(urls,))
            t.start() # fetching_data(urls)
            # Append the thread in the pool
            threads.append(t)
            time.sleep(0.1)
            print(f"{property_type} batch number {i} : DONE")
            i += 1

    print(time.time() - start)
    data = []

    for thread in threads:
        while thread.is_alive():
            time.sleep(0.5)
        data.extend(thread.data)
        print(f"Thread of length {len(thread.data)} completed")

    print(time.time() - start)
    driver.close()

    df = raw_to_csv(data)
    clean_to_csv(df)

if __name__ == '__main__':
    main()
