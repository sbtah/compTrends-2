from typing import Dict, List
from scraper.logic.api_scrapers.api_scraper import ApiScraper


class LeroyMerlinApiScraper(ApiScraper):
    """
    Api Scraper for Leroy Merlin store.
    """

    all_stores_endpoint = "https://www.leroymerlin.pl/www/ajax/shop/all.html"
    single_product_for_store = "https://www.leroymerlin.pl/www/ajax/productStockAndPrice.html?instalments=true&productId={}&store={}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_local_stores(self, *args, **kwargs):
        return super().get_local_stores(self.all_stores_endpoint)