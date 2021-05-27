import pandas as pd
import os.path

parent_path = os.path.abspath("../")

def convert_to_csv(list_of_properties):
    '''
    a function that will create a CSV file with the provided list of properties ( estates )
    user needs to specify file name, the file is created in the root directory

    :param list_of_properties: a list of dictionaries containing the properties
    '''
    print("choose file name:")
    file_name = input()
    table_of_properties = pd.DataFrame(list_of_properties)
    table_of_properties.to_csv(os.path.join(parent_path, f"{file_name}.csv"))

# test_data = [{"id":1,"first_name":"Lisetta","last_name":"Rowett","email":"lrowett0@ed.gov","gender":"Genderfluid"},
#     {"id":2,"first_name":"Swen","last_name":"O'Noulane","email":"sonoulane1@clickbank.net","gender":"Male"},
#     {"id":3,"first_name":"Bertrando","last_name":"Cancutt","email":"bcancutt2@baidu.com","gender":"Polygender"},
#     {"id":4,"first_name":"Stacee","last_name":"Maeer","email":"smaeer3@paginegialle.it","gender":"Male"},
#     {"id":5,"first_name":"Bernhard","last_name":"Mingame","email":"bmingame4@myspace.com","gender":"Bigender"}]

# convert_to_csv(test_data)
