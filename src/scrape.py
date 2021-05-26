import json
import os
import requests
from bs4 import BeautifulSoup
import re
#import lxml
#import time

item_url = 'https://www.immoweb.be/en/classified/house/for-sale/uccle/1180/9310971?searchId=60acaf3b768b5'
r = requests.get(item_url)
print(item_url, r.status_code)
item_soup = BeautifulSoup(r.content,'html5lib')
#print(item_soup)
item_script = item_soup.select('#container-main-content div script')
# item_string is bs4.element.Tag
item_string = str(item_script[0])
# so we cut the useful part of it to get a JSON string
item_JSON = item_string[64:-19]
# converting string to a Python dictionary
item_parse = json.loads(item_JSON)
#print(item_parse)
item_id = item_parse['id']
item_seller = item_parse['customers']
item_property = item_parse['property']
item_price_all = item_parse['price']
#item_transcactions = item_parse['transactions']

item_adress = item_property['location']['street'] + item_property['location']['number']
item_property_type = item_property['type']
item_property_subtype = item_property['subtype']
item_price = item_price_all['mainValue']
#item_type_of_sale = [item_transcactions['subtype'],item_transcactions['lifeAnnuity']]
item_number_of_rooms = item_property['bedroomCount']
item_area = item_property['netHabitableSurface']

print(item_property_type, item_property_subtype, item_price, item_number_of_rooms, item_area)
#item_kitchen = item_property['kitchen']
#item_furnished
#item_open_fire
#item_terrace
#item_garden
#item_geo
#item_facades
#item_swimming_pool
#item_situation
