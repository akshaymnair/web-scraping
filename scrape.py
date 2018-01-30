from bs4 import BeautifulSoup
import urllib3
import sys
import re


class Scrape:
    def __init__(self):
        urllib3.disable_warnings()
        self.http = urllib3.PoolManager()

    def scrape(self, url):
        try:
            page = self.http.request('GET', url)
        except urllib3.exceptions.HTTPError as e:
            print("Http Error: "+str(e.reason))
            sys.exit(1)
        return page

    def fetch_text_content(self, element):
        if element:
            return element.text
        else:
            ""

    def is_verified(self, element):
        #print(element)
        if element:
            return True
        else:
            return False

    def extract_phone_specs(self, page):
        if page.status == 200:
            spec_json = dict()
            soup = BeautifulSoup(page.data, 'lxml')
            # phone name
            spec_json['product_name'] = self.fetch_text_content(soup.find('h1', {"class": "specs-phone-name-title"}))
            spec_json['product_type'] = 'phone'
            spec = soup.find_all('div', id='specs-list')
            spec_soup = BeautifulSoup(str(spec), 'lxml')
            # network
            spec_json['network_2g'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "net2g"}))
            spec_json['network_3g'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "net3g"}))
            spec_json['network_4g'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "net4g"}))
            spec_json['network_speed'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "speed"}))
            spec_json['network_gprs_support'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "gprstext"}))
            spec_json['network_edge_support'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "edge"}))
            # launch
            spec_json['launch_announced'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "year"}))
            spec_json['launch_availability'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "status"}))
            # body
            spec_json['body_dimensions'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "dimensions"}))
            spec_json['body_weight'] = self.fetch_text_content(spec_soup.find('td', {"data-spec": "weight"}))
            spec_json['body_build'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "build"}))
            spec_json['body_sim'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "sim"}))
            spec_json['body_other'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "bodyother"}))
            # display
            spec_json['display_type'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "displaytype"}))
            spec_json['display_size'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "displaysize"}))
            spec_json['display_resolution'] =self.fetch_text_content(
                spec_soup.find('td', {"data-spec": "displayresolution"}))
            spec_json['display_protection'] =self.fetch_text_content(
                spec_soup.find('td', {"data-spec": "displayprotection"}))
            spec_json['display_other'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "displayother"}))
            # platform
            spec_json['platform_os'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "os"}))
            spec_json['platform_chipset'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "chipset"}))
            spec_json['platform_cpu'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "cpu"}))
            spec_json['platform_gpu'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "gpu"}))
            # memory
            spec_json['memory_slot'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "memoryslot"}))
            spec_json['internal_memory'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "internalmemory"}))
            # camera
            spec_json['camera_primary'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "cameraprimary"}))
            spec_json['camera_features'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "camerafeatures"}))
            spec_json['camera_video'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "camera_video"}))
            spec_json['camera_secondary'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "camerasecondary"}))
            # comms
            spec_json['comms_wlan'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "wlan"}))
            spec_json['comms_bluetooth'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "bluetooth"}))
            spec_json['comms_gps'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "gps"}))
            spec_json['comms_nfc'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "nfc"}))
            spec_json['comms_radio'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "radio"}))
            spec_json['comms_usb'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "usb"}))
            # features
            spec_json['features_sensor'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "sensor"}))
            spec_json['features_other'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "featuresother"}))
            # battery
            spec_json['battery_description'] =self.fetch_text_content(
                spec_soup.find('td', {"data-spec": "batdescription1"}))
            spec_json['battery_talk_time'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "battalktime1"}))
            spec_json['battery_music_playback'] =self.fetch_text_content(
                spec_soup.find('td', {"data-spec": "batmusicplayback1"}))
            spec_json['comms_usb'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "usb"}))
            # misc
            spec_json['misc_colors'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "misccolors"}))
            spec_json['misc_sar_us'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "sar-us"}))
            spec_json['misc_sar_eu'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "sar-eu"}))
            spec_json['misc_price'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "price"}))
            # benchmarks
            spec_json['bench_tbench'] =self.fetch_text_content(spec_soup.find('td', {"data-spec": "tbench"}))
            spec_json['reviews'] = []
            return spec_json

    def extract_amazon_reviews(self, page):
        if page.status == 200:
            soup = BeautifulSoup(page.data, 'lxml')
            reviews = soup.find_all('div', {"data-hook":"review"})
            rev_string = ''
            rev_array = []
            for review in reviews:
                rev_json = dict()
                review_soup = BeautifulSoup(str(review), 'lxml')
                rev_json['body'] = self.fetch_text_content(review_soup.find('span', {"data-hook": "review-body"}))
                rev_json['title'] = self.fetch_text_content(review_soup.find('a', {"data-hook": "review-title"}))
                rev_json['star_rating'] = str(self.fetch_text_content(review_soup.find('span', {"class": "a-icon-alt"}))[:1])
                rev_json['author'] = self.fetch_text_content(review_soup.find('a', {"data-hook": "review-author"}))
                rev_json['date'] = str(self.fetch_text_content(review_soup.find('span', {"data-hook": "review-date"})))[3:]
                votes = str(self.fetch_text_content(review_soup.find('span', {"data-hook": "helpful-vote-statement"})))
                votes = re.findall(r'\d+', votes)
                rev_json['votes'] = (votes or [None])[0]
                rev_json['verified_purchase'] = self.is_verified(review_soup.find('span', {"data-hook": "avp-badge"}))
                rev_string += str(rev_json) + '\n'
                rev_array.append(rev_json)
            return rev_array