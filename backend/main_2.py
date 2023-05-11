
"""
Used for local testing.
"""
import httpx
from urllib.parse import urlsplit
import time
import re
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper


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


with LeroyMerlinScraper(requested_url='https://www.leroymerlin.pl/izolacja-budynkow/kleje-uszczelniacze-izolacje/tasmy-uszczelniajace-do-wnetrz,a1491.html', store_url="https://www.leroymerlin.pl/") as scraper:
    res_el = scraper.visit_page(url=scraper.requested_url)
    element = scraper.find_element(html_element=res_el, xpath_to_search='.//ul[@class="menu-list"]/li[contains(@class, "mega-world-item")]')
    print(element)
    print(element.text_content())
    extracted = scraper.extract_text(element=element)
    print(extracted)