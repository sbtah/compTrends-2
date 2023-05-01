from scraper.stores.leroy_merlin.leroy_selenium import LeroyMerlinSeleniumScraper
from scraper.stores.leroy_merlin.leroy_api import LeroyMerlinApiScraper


class LeroyMerlin:
    """"""

    selenium_scraper = LeroyMerlinSeleniumScraper()
    api_scraper = LeroyMerlinApiScraper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)