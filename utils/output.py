import time

def threads_to_dict(threads):
    for thread in threads:
        while thread.is_alive():
            time.sleep(4)

def raw_to_csv():
    pass

def clean_to_csv():
    pass

def cleaning():
    pass