import time
from utils.output import backup, cleaning
from utils.fetching import fetching_data, fetching_urls
from selenium import webdriver



def main():
    driver = webdriver.Safari()

    fetching_urls()

    time.sleep(1)

    fetching_data()

    backup()

    cleaning()

    driver.close()

    pass


if __name__ == '__main__':
    main()