import pandas as pd
import os.path
from typing import List, Dict, Union, Optional

def convert_to_csv(list_of_properties: List[Dict[str, Optional[Union[str,float,int]]]]) -> None:
    '''
    a function that will create a CSV file with the provided list of properties ( estates )
    user needs to specify file name, the file is created in the root directory

    :param list_of_properties: a list of dictionaries containing the properties
    '''
    print("choose file name:")
    file_name = input()
    table_of_properties = pd.DataFrame(list_of_properties)
    table_of_properties.to_csv(f"{file_name}.csv")
