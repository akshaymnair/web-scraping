import sys
import scrape

STORAGE_PATH = 'specs/'
SPECS_FILE_NAME = 'specs.txt'
PHONE_LIST = 'phone_list.txt'
GSM_ARENA_BASE_URL = "https://www.gsmarena.com/"


def fetch_phone_list():
    try:
        with open(PHONE_LIST) as f:
            phones = f.readlines()
        phones = [x.strip().replace('\n', '') for x in phones]
    except IOError:
        print('\n' + 'No phone list to iterate. ' + '\n')
        sys.exit(1)
    return phones


def main():
    phones = fetch_phone_list()
    scrape_obj = scrape.Scrape()

    # TODO remove
    f = open(STORAGE_PATH + SPECS_FILE_NAME, 'w')

    for phone in phones:
        print(phone)
        page = scrape_obj.scrape(GSM_ARENA_BASE_URL + phone)
        # TODO update db
        f.write(str(scrape_obj.extract_phone_specs(page)) + "\n")

    # TODO remove
    f.close()

if __name__ == "__main__":
    main()
