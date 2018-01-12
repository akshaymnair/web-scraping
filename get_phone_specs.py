import urllib3
from bs4 import BeautifulSoup
import sys

urllib3.disable_warnings()

def fetchTextContent(element):
    if element:
        return element.text
    else:
        ""

storage_path = 'specs/'
file_name = 'specs.txt'
phone_list = 'phone_list.txt'
base_url = "https://www.gsmarena.com/"

try:
    with open(phone_list) as f:
        phones = f.readlines()
    phones = [x.strip().replace('\n', '') for x in phones]
except IOError:
    print('\n' + 'No phone list to iterate. ' + '\n')
    sys.exit(1)

f = open(storage_path + file_name, 'w')
for phone in phones:
    print(phone)
    http = urllib3.PoolManager()
    page = http.request('GET', base_url + phone)
    spec_json = {}
    if page.status == 200:
        soup = BeautifulSoup(page.data, 'lxml')
        spec = soup.find_all('div', id='specs-list')
        spec_soup = BeautifulSoup(str(spec), 'lxml')
        #network
        spec_json['network_2g'] = fetchTextContent(spec_soup.find('td',{"data-spec" : "net2g"}))
        spec_json['network_3g'] = fetchTextContent(spec_soup.find('td', {"data-spec": "net3g"}))
        spec_json['network_4g'] = fetchTextContent(spec_soup.find('td', {"data-spec": "net4g"}))
        spec_json['network_speed'] = fetchTextContent(spec_soup.find('td', {"data-spec": "speed"}))
        spec_json['network_gprs_support'] = fetchTextContent(spec_soup.find('td', {"data-spec": "gprstext"}))
        spec_json['network_edge_support'] = fetchTextContent(spec_soup.find('td', {"data-spec": "edge"}))
        #launch
        spec_json['launch_announced'] = fetchTextContent(spec_soup.find('td', {"data-spec": "year"}))
        spec_json['launch_availability'] = fetchTextContent(spec_soup.find('td', {"data-spec": "status"}))
        #body
        spec_json['body_dimensions'] = fetchTextContent(spec_soup.find('td', {"data-spec": "dimensions"}))
        spec_json['body_weight'] = fetchTextContent(spec_soup.find('td', {"data-spec": "weight"}))
        spec_json['body_build'] = fetchTextContent(spec_soup.find('td', {"data-spec": "build"}))
        spec_json['body_sim'] = fetchTextContent(spec_soup.find('td', {"data-spec": "sim"}))
        spec_json['body_other'] = fetchTextContent(spec_soup.find('td', {"data-spec": "bodyother"}))
        #display
        spec_json['display_type'] = fetchTextContent(spec_soup.find('td', {"data-spec": "displaytype"}))
        spec_json['display_size'] = fetchTextContent(spec_soup.find('td', {"data-spec": "displaysize"}))
        spec_json['display_resolution'] = fetchTextContent(spec_soup.find('td', {"data-spec": "displayresolution"}))
        spec_json['display_protection'] = fetchTextContent(spec_soup.find('td', {"data-spec": "displayprotection"}))
        spec_json['display_other'] = fetchTextContent(spec_soup.find('td', {"data-spec": "displayother"}))
        #platform
        spec_json['platform_os'] = fetchTextContent(spec_soup.find('td', {"data-spec": "os"}))
        spec_json['platform_chipset'] = fetchTextContent(spec_soup.find('td', {"data-spec": "chipset"}))
        spec_json['platform_cpu'] = fetchTextContent(spec_soup.find('td', {"data-spec": "cpu"}))
        spec_json['platform_gpu'] = fetchTextContent(spec_soup.find('td', {"data-spec": "gpu"}))
        #memory
        spec_json['memory_slot'] = fetchTextContent(spec_soup.find('td', {"data-spec": "memoryslot"}))
        spec_json['internal_memory'] = fetchTextContent(spec_soup.find('td', {"data-spec": "internalmemory"}))
        #camera
        spec_json['camera_primary'] = fetchTextContent(spec_soup.find('td', {"data-spec": "cameraprimary"}))
        spec_json['camera_features'] = fetchTextContent(spec_soup.find('td', {"data-spec": "camerafeatures"}))
        spec_json['camera_video'] = fetchTextContent(spec_soup.find('td', {"data-spec": "camera_video"}))
        spec_json['camera_secondary'] = fetchTextContent(spec_soup.find('td', {"data-spec": "camerasecondary"}))
        #comms
        spec_json['comms_wlan'] = fetchTextContent(spec_soup.find('td', {"data-spec": "wlan"}))
        spec_json['comms_bluetooth'] = fetchTextContent(spec_soup.find('td', {"data-spec": "bluetooth"}))
        spec_json['comms_gps'] = fetchTextContent(spec_soup.find('td', {"data-spec": "gps"}))
        spec_json['comms_nfc'] = fetchTextContent(spec_soup.find('td', {"data-spec": "nfc"}))
        spec_json['comms_radio'] = fetchTextContent(spec_soup.find('td', {"data-spec": "radio"}))
        spec_json['comms_usb'] = fetchTextContent(spec_soup.find('td', {"data-spec": "usb"}))
        #features
        spec_json['features_sensor'] = fetchTextContent(spec_soup.find('td', {"data-spec": "sensor"}))
        spec_json['features_other'] = fetchTextContent(spec_soup.find('td', {"data-spec": "featuresother"}))
        #battery
        spec_json['battery_description'] = fetchTextContent(spec_soup.find('td', {"data-spec": "batdescription1"}))
        spec_json['battery_talk_time'] = fetchTextContent(spec_soup.find('td', {"data-spec": "battalktime1"}))
        spec_json['battery_music_playback'] = fetchTextContent(spec_soup.find('td', {"data-spec": "batmusicplayback1"}))
        spec_json['comms_usb'] = fetchTextContent(spec_soup.find('td', {"data-spec": "usb"}))
        #misc
        spec_json['misc_colors'] = fetchTextContent(spec_soup.find('td', {"data-spec": "misccolors"}))
        spec_json['misc_sar_us'] = fetchTextContent(spec_soup.find('td', {"data-spec": "sar-us"}))
        spec_json['misc_sar_eu'] = fetchTextContent(spec_soup.find('td', {"data-spec": "sar-eu"}))
        spec_json['misc_price'] = fetchTextContent(spec_soup.find('td', {"data-spec": "price"}))
        #benchmarks
        spec_json['bench_tbench'] = fetchTextContent(spec_soup.find('td', {"data-spec": "tbench"}))

        #TODO update database
        print(str(spec_json))
f.close



