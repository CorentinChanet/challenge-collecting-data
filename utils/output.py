import time

def _threads_to_dict(threads):
    items = []
    for thread in threads:
        fields = ("Type", "Subtype", "Price", "Number of rooms", "Area", "Fully equipped kitchen",
                  "Furnished", "Open Fire", "Terrace", "Plot size", "Number of facades", "Swimming pool", "State")
        while thread.is_alive():
            time.sleep(3)

        item = {field: value for field, value in zip(fields, thread.data)}
        items.append(item)
    return items

def raw_to_csv():
    pass

def clean_to_csv():
    pass

def cleaning():
    pass