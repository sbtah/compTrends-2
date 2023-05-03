from scraper.logic.selenium_scrapers.ecommerce import EcommerceSeleniumScraper
from urllib.parse import urljoin


class LeroyMerlinScraper(EcommerceSeleniumScraper):
    """
    Master class for LeroyMerlin store, that wraps Selenium and Api scrapers.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_all_local_stores(self):
        pass

    def get_all_categories(self):
        pass

    def get_all_products(self):
        pass

    @property
    def potenial_popups_xpaths(self):
        return ['//div[@id="yourcx_layer"]//a[@class="yourcx_close"]',]

    @property
    def cookies_close_xpath(self):
        return './/button[contains(@id, "onetrust-accept")]'

    @property
    def store_picked_xpath(self):
        return './/ul[@class="user-navbar"]/li[@class="top-shop-details"]/a[@data-shop-name]/@data-shop-name'

    def categories_map(self) -> dict:
        return {
            "0": {
                "category_xpath": './/div[@class="mega-menu-content"]/ul[contains(@class, "mega-world-items")]/li[contains(@class, "menu-item")]',
                "category_parser": self.parse_level_0_category_element,
            },
            "1": {
                "category_xpath": './/nav[contains(@class, "dropdown-menu")]/div[@class="dropdown-menu-wrapper"]//ul[contains(@class, "dropdown-list")]/li[@class="dropdown-item"]',
                "category_parser": self.parse_level_1_category_element,
            },
            "2": {
                "category_xpath": './/div[@class="list"]/h2',
                "category_parser": self.parse_level_2_category_element,
            },
            "3": {
                "category_xpath": './/ul[@class="menu"]/li[contains(@class, "category-item") and not(contains(@class, "active"))]',
                "category_parser": self.parse_level_3_category_element,
            },
        }

    def parse_level_0_category_element(self, html_element):
        url = html_element.xpath('./a[@class="menu-link products"]/@href')[0]
        name = html_element.xpath('./a[@class="menu-link products"]/span/text()')[0]
        return urljoin(self.store_url, url), name.strip()

    def parse_level_1_category_element(self, html_element):
        url = html_element.xpath('./a[contains(@class, "dropdown-link")]/@href')[0]
        name = html_element.xpath('./a[contains(@class, "dropdown-link")]/text()')[0]
        return urljoin(self.store_url, url), name.strip()

    def parse_level_2_category_element(self, html_element):
        url = html_element.xpath('./a[@data-ua]/@href')[0]
        name = html_element.xpath('./a[@data-ua]/text()')[0]
        return urljoin(self.store_url, url), name.strip()

    def parse_level_3_category_element(self, html_element):
        url = html_element.xpath('./a/@href')[0]
        name = html_element.xpath('./a/text()')[0]
        return urljoin(self.store_url, url), name.strip()

    def pick_local_store_by_name(self, store_name, html_element):
        # Initialize store picker
        self.find_and_click_selenium_element(
            html_element=html_element,
            xpath_to_search='.//a[contains(@class, "button-shop-details")]',
        )
        new_element = self.generate_html_element()
        # Initialize Input
        self.find_and_click_selenium_element(
            html_element=new_element,
            xpath_to_search='.//span[@class="select2-selection__arrow" and @role="presentation"]',
        )
        # Find input
        input_el = self.find_selenium_element(xpath_to_search='.//input[@type="search" and @class="select2-search__field"]')
        # Pick store by name
        self.send_text_to_element(text=store_name, selenium_element=input_el)
        # Click confirm button
        newest_element = self.generate_html_element()
        self.find_and_click_selenium_element(
            html_element=newest_element,
            xpath_to_search='.//button[contains(@class, "shop-details-set-button") and @data-shop-id]',
        )
        return self.validate_store_picked(store_name=store_name)