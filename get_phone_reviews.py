import sys
import scrape
import mongo
from utils import fetch_phone_list
from properties import REVIEW_STORAGE_PATH
from properties import REVIEWS_FILE_NAME
from properties import AMAZON_BASE_URL
from properties import AMAZON_REVIEW_URL_1

def main():
    scrape_obj = scrape.Scrape()
    phones = fetch_phone_list()
    print('Fetching reviews from amazon : ')

    for phone in phones:
        # TODO remove
        f = open(REVIEW_STORAGE_PATH + phone[0] + '.txt', 'a', encoding='utf-8')
        count = 1
        page = scrape_obj.scrape(AMAZON_BASE_URL + phone[2] + AMAZON_REVIEW_URL_1 + str(count))
        print(phone[0])
        while page.status == 200:
            # TODO update db
            extracted_reviews = scrape_obj.extract_amazon_reviews(page)
            if not extracted_reviews:
                break
            f.write(str(extracted_reviews))
            mongo.update_phone_reviews(extracted_reviews, phone[0])
            count += 1
            page = scrape_obj.scrape(AMAZON_BASE_URL + phone[2] + AMAZON_REVIEW_URL_1 + str(count))
        # TODO remove
        f.close()

if __name__ == "__main__":
    main()
