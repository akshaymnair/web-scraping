import sys
import scrape
import mongo
from utils import  fetch_phone_list
from properties import SPECS_STORAGE_PATH
from properties import SPECS_FILE_NAME
from properties import GSM_ARENA_BASE_URL

def main():
    phones = fetch_phone_list()
    scrape_obj = scrape.Scrape()
    print('Fetching phone specs from gsm arena : ')
    # TODO remove
    f = open(SPECS_STORAGE_PATH + SPECS_FILE_NAME, 'w', encoding='utf-8')

    for phone in phones:
        print('Fetching %s phone specs from gsm arena' % phone[0])
        page = scrape_obj.scrape(GSM_ARENA_BASE_URL + phone[1], '', '')
        specs = scrape_obj.extract_phone_specs(page)
        # TODO update db
        mongo.insert_phone_specs(specs)
        f.write(str(specs) + "\n")

    # TODO remove
    f.close()

if __name__ == "__main__":
    main()
