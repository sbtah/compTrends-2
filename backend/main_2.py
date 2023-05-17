
"""
Used for local testing.
"""
import httpx
from urllib.parse import urlsplit
import time
import re
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper
from utilities.loader import ScraperLoader

# 'app-platform': 'new.leroymerlin.pl'
#url = "https://new.leroymerlin.pl/microservices/proxy-api-service/v1/catalog/search-products-filters?node=156&searchView=false&spellcheck=false"
#4pHgXxEx7CrM_T_yKTYsd
# headers = {'storeCode': '104', 'Sec-Fetch-Site': 'same-origin', 'app-platform': '9BZMQ-MSBTM-TBZA5-5Q75N-X95UD'}
#headers = {'storeCode': '22', 'userIdHash': "%7B%7D", 'app-platform': 'RWD'}
#res = httpx.get(url="https://new.leroymerlin.pl/microservices/proxy-api-service/v1/products/45122462/store/available-quantity" , headers=headers)
# res_2 = httpx.get(url="https://new.leroymerlin.pl/microservices/proxy-api-service/v1/catalog/search-products-filters?node=156&searchView=false&spellcheck=false", headers=headers)
# print(res_2.text)
#if 'new' in (urlsplit(url).netloc):
#    print('new')


loader = ScraperLoader(package='leroy_merlin', module_name='leroy_merlin', class_name='LeroyMerlinScraper')
scraper = loader.import_scraper()
print(scraper)