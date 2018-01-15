import sys
import scrape

storage_path = 'specs/'
file_name = 'specs.txt'
phone_list = 'phone_list.txt'
base_url = "https://www.gsmarena.com/"


def fetch_phone_list():
    try:
        with open(phone_list) as f:
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
    f = open(storage_path + file_name, 'w')

    for phone in phones:
        print(phone)
        page = scrape_obj.scrape(base_url + phone)
        # TODO update db
        f.write(str(scrape_obj.extract_phone_specs(page)) + "\n")

    # TODO remove
    f.close()


if __name__ == "__main__":
    main()
