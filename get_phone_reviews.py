import sys
import scrape

STORAGE_PATH = 'reviews/'
#Filename to be changed for each phone.
REVIEWS_FILE_NAME = 'reviews.txt'
#Url hardcoded now. Please change eah time.
AMAZON_URL = "https://www.amazon.com/Samsung-Galaxy-S8-Unlocked-64GB/product-reviews/B06Y14T5YW/ref=cm_cr_arp_d_paging_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="
#AMAZON_URL = "https://www.amazon.com/Google-Pixel-Phone-display-Unlocked/product-reviews/B01M01YX15/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="
def main():
    scrape_obj = scrape.Scrape()
    # TODO remove
    f = open(STORAGE_PATH + REVIEWS_FILE_NAME, 'a',encoding='utf-8')
    count = 1
    page = scrape_obj.scrape(AMAZON_URL + str(count))
    while page.status == 200:
        scrape_obj.extract_reviews(page)
        # TODO update db
        extracted_reviews = scrape_obj.extract_reviews(page)
        if not extracted_reviews:
            break
        f.write(str(extracted_reviews))
        count += 1
        page = scrape_obj.scrape(AMAZON_URL + str(count))
    # TODO remove
    f.close()

if __name__ == "__main__":
    main()
