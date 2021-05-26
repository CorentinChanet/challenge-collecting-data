import time
import random
from utils.output import raw_to_csv, clean_to_csv, cleaning
from utils.fetching import fetching_urls, fetching_data, select_driver
from selenium import webdriver
from threading import Thread


def main():

    driver_name = input("Select webdriver: safari, chrome or firefox")

    threads = list()

    i=1
    while i<3:
        url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={i}&orderBy=newest"
        urls = fetching_urls(url, driver_name)
        t = Thread(name='Test {}'.format(i), target=fetching_data, args=(urls,))
        t.start() # fetching_data(urls)
        threads.append(t)
        time.sleep(0.5 + random.random())
        print(i)
        i += 1
        time.sleep(0.5 + random.random())

    #raw_to_csv()

    #cleaning()

    #clean_to_csv()

    #driver.close()

    pass


if __name__ == '__main__':
    main()