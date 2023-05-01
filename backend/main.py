"""
Used for local testing.
"""
import time
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper




scraper = LeroyMerlinScraper()


page = scraper.selenium_scraper.selenium_get(url='https://www.leroymerlin.pl/')
element = scraper.selenium_scraper.generate_html_element()
scraper.selenium_scraper.close_cookies_banner(html_element=element)
new_el = scraper.selenium_scraper.generate_html_element()


scraper.selenium_scraper.pick_local_store_by_name(store_name="Bielsko-Biała", html_element=new_el)
scraper.selenium_scraper.quit_and_clean()