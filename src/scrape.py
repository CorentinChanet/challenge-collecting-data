import time
import re
from bs4 import BeautifulSoup
import requests
import os
import json
urls_all = ['https://www.immoweb.be/en/classified/house/for-sale/oudenaarde/9700/9350213?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/mixed-use-building/for-sale/aartselaar/2630/9350212?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/wilrijk/2610/9350208?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/huy/4500/9350202?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/lier/2500/9350201?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/mansion/for-sale/waregem/8790/9350183?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/mansion/for-sale/waregem/8790/9350182?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/waregem/8790/9350181?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/desselgem/8792/9350180?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/holsbeek/3220/9350176?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/apartment-block/for-sale/gent/9000/9350175?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/tremelo/3120/9285264?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/ekeren/2180/9350141?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/destelbergen/9070/9322199?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/mansion/for-sale/antwerp/2018/9350133?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/country-cottage/for-sale/aische-en-refail/5190/9350132?searchId=60ae3be4040a2',
            'https://www.immoweb.be/en/classified/house/for-sale/kortrijk/8500/9350131?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/stabroek/2940/9350127?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/schoten/2900/9280605?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/somzee/5651/9350126?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/ath/7800/9350125?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/evergem/9940/9350111?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/auderghem/1160/9350102?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/borgerhout/2140/9350099?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/mechelen/2800/9350097?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/soignies-(horrues)/7060/9350089?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/grimbergen/1850/9350088?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/boom/2850/9258513?searchId=60ae3be4040a2', 'https://www.immoweb.be/en/classified/house/for-sale/laakdal/2430/9350086?searchId=60ae3be4040a2']
urls = []
for i in range(1, 4):
    urls.append(urls_all[i])
# print(urls)

#import lxml


def fetching_data(url:str):

    item_url = url
    r = requests.get(item_url)
    #print(item_url, r.status_code)
    item_soup = BeautifulSoup(r.content, 'html5lib')
    # print(item_soup)
    item_script = item_soup.select('#container-main-content div script')
    # item_string is bs4.element.Tag
    item_string = str(item_script[0])
    # so we cut the useful part of it to get a JSON string
    item_JSON = item_string[64:-19]
    # converting string to a Python dictionary
    item_parse = json.loads(item_JSON)
    # print(item_parse)
    item_id = item_parse['id']
    item_seller = item_parse['customers']
    item_property = item_parse['property']
    item_price_all = item_parse['price']
    item_transcactions = item_parse['transaction']

    
    item_street = item_property['location']['street']
    item_street_number = item_property['location']['number']
    item_property_type = item_property['type']
    item_property_subtype = item_property['subtype']
    item_price = item_price_all['mainValue']
    #item_type_of_sale = [item_transcactions['subtype'],item_transcactions['lifeAnnuity']]
    item_number_of_rooms = item_property['bedroomCount']
    item_area = item_property['netHabitableSurface']
    # INSTALLED, USA_HYPER_EQUIPPED, USA_INSTALLED
    item_kitchen = item_property['kitchen']
    item_kitchen_check = item_property['kitchen']['type']
    if "equipped" in item_kitchen_check:
        item_kitchen = 'yes'
    

    print(f'\nPropery type and subtype is {item_property_type} {item_property_subtype}, located at {item_street} {item_street_number}, price is {item_price}, it has {item_number_of_rooms} rooms and {item_area} area, kitchen is {item_kitchen_check}')
    
    return item_property_type, item_property_subtype, item_price, item_number_of_rooms, item_area
    # item_furnished
    # item_open_fire
    # item_terrace
    # item_garden
    # item_geo
    # item_facades
    # item_swimming_pool
    # item_situation
    time.sleep(2)
    print("DATA FETCHED! : " + str(url))


# basic
fetching_data('https://www.immoweb.be/en/classified/exceptional-property/for-sale/orp-jauche/1350/9308169?searchId=60ae3eb719d5a')
#test
#fetching_data('https://www.immoweb.be/en/classified/house/for-sale/les-mazures/08500/9350378')
