import pandas as pd
import os.path
from typing import List, Dict, Union, Optional

def raw_to_csv(list_of_properties: List[Dict[str, Optional[Union[str,float,int]]]]) -> None:
    '''
    A function that will create two CSV files with the provided list of properties ( estates ).
    User needs to specify each file name (raw and clean), the file is created in the same directory as main.py.

    :param list_of_properties: a list of dictionaries containing the properties
    '''
    print("choose raw_table file name:")
    file_name = input()
    raw_table = pd.DataFrame(list_of_properties)
    raw_table.to_csv(f"{file_name}.csv")

    print("choose clean_table file name:")
    file_name = input()
    clean_table = _cleaner(raw_table)
    clean_table.to_csv(f"{file_name}.csv")

def _cleaner(table: pd.DataFrame) -> pd.DataFrame:
    # Function that will clean the panda table and create a corresponding csv file
    pass