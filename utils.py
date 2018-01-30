import sys
from properties import PHONE_LIST

def fetch_phone_list():
    try:
        with open(PHONE_LIST) as f:
            phones = f.readlines()
        phones = [x.strip().replace('\n', '').split('::') for x in phones]
    except IOError:
        print('\n' + 'No phone list to iterate. ' + '\n')
        sys.exit(1)
    return phones