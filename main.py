import time
from utils.output import raw_to_csv, clean_to_csv, cleaning
from utils.fetching import fetching_data, fetching_urls
from selenium import webdriver



def main():
    driver = webdriver.Safari()

    fetching_urls()

    time.sleep(1)

    fetching_data()

    raw_to_csv()

    cleaning()

    clean_to_csv()

    driver.close()

    pass


if __name__ == '__main__':
    main()