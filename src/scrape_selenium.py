import time
import re
import random
from selenium import webdriver
driver = webdriver.Firefox()

#driver.get("https://immo.vlan.be/en/detail/flat---apartment/for-sale/2390/oostmalle/ray96637")
driver.get("https://www.immoweb.be/en/search/house/for-sale?countries=BE&orderBy=newest")

time.sleep(random.random())

element_XPATH = '//*[@id="main-content"]'
house_links = []
element_ul = driver.find_element_by_xpath(element_XPATH)
for a in element_ul.find_elements_by_tag_name('a'):
    house_links.append(a.get_attribute('href'))
    print(house_links)

driver.close()


"""
for i in range(1, 34):
    house_link = '/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/ul/li[' + str(i) + ']/article/div[1]/h2/a'
    house_links_XPATH.append(house_link)
    driver_house_link = driver.find_element_by_xpath(house_links).get_attribute('href') 
    house_links.append(driver_house_link)
    

#last_house_at_page_link_XPATH = '/html/body/div[1]/div[2]/div/main/div/div[2]/div/div[3]/div/div/div[1]/div/ul/li[33]/article/div[1]/h2/a'

time.sleep(random.random())


#print(house_links_XPATH[5])
#print(house_links[5])

"""

