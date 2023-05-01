"""
Used for local testing.
"""
import time
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper




scraper = LeroyMerlinScraper()


element = scraper.selenium_scraper.visit_page(url='https://www.leroymerlin.pl/')
scraper.selenium_scraper.pick_local_store_by_name(store_name="Bielsko-Biała", html_element=element)
scraper.selenium_scraper.quit_and_clean()