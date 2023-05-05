"""
Used for local testing.
"""
import time
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper



scraper = LeroyMerlinScraper(
    requested_url="https://www.leroymerlin.pl/",
    store_url="https://www.leroymerlin.pl/"
)

element = scraper.visit_page(url=scraper.requested_url)
store_button = scraper.find_selenium_element(xpath_to_search=scraper.cookies_close_xpath)
print(scraper.extract_text(element=store_button))
