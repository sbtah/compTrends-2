from scraper.stores.leroy_merlin.leroy_selenium import LeroyMerlinSeleniumScraper
from scraper.stores.leroy_merlin.leroy_api import LeroyMerlinApiScraper


class LeroyMerlinScraper:
    """
    Master class for LeroyMerlin store, that wraps Selenium and Api scrapers.
    """

    selenium_scraper = LeroyMerlinSeleniumScraper()
    api_scraper = LeroyMerlinApiScraper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_all_local_stores(self):
        pass

    def get_all_categories(self):
        pass

    def get_all_products(self):
        pass
