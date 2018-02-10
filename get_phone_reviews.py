import sys
import scrape
import mongo
from utils import fetch_phone_list
from properties import REVIEW_STORAGE_PATH
from properties import AMAZON_BASE_URL
from properties import AMAZON_REVIEW_URL_1
from properties import FLIPKART_REQUEST_FIELDS
from properties import HEADERS
from properties import FLIPKART_REVIEW_URL


def main():
    phones = fetch_phone_list()

    get_amazon_reviews(phones)
    get_flipkart_reviews(phones)


def get_amazon_reviews(phones):
    scrape_obj = scrape.Scrape()
    for phone in phones:
        count = 1
        page = scrape_obj.scrape(AMAZON_BASE_URL + phone[2] + AMAZON_REVIEW_URL_1 + str(count), '', '')
        print('Fetching amazon reviews for %s' % phone[0])
        while page.status == 200:
            extracted_reviews = scrape_obj.extract_amazon_reviews(page)
            if not extracted_reviews:
                break
            mongo.update_phone_reviews(extracted_reviews, phone[0])
            count += 1
            page = scrape_obj.scrape(AMAZON_BASE_URL + phone[2] + AMAZON_REVIEW_URL_1 + str(count), '', '')


def get_flipkart_reviews(phones):
    scrape_obj = scrape.Scrape()
    fields = FLIPKART_REQUEST_FIELDS
    for phone in phones:
        fields['productId'] = phone[3]
        page = scrape_obj.scrape(FLIPKART_REVIEW_URL, fields, HEADERS)
        print('Fetching flipkart reviews for %s' % phone[0])
        if page.status == 200:
            extracted_reviews = scrape_obj.extract_flipkart_reviews(page)
            if not extracted_reviews:
                break
            mongo.update_phone_reviews(extracted_reviews, phone[0])

if __name__ == "__main__":
    main()
