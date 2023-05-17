import re
from urllib.parse import urljoin, urlsplit

from scraper.logic.selenium_scrapers.ecommerce import EcommerceSeleniumScraper


class LeroyMerlinScraper(EcommerceSeleniumScraper):
    """
    Master class for LeroyMerlin store, that wraps Selenium and Api scrapers.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract_category_id_from_url(self, url):
        match = re.search(r'a(\d+)\.html', url)
        category_id = int(match.group(1))
        return category_id

    def extract_product_id_from_url(self, url):
        match = re.search(r',p(\d+),', url)
        product_id = int(match.group(1))
        return product_id

    @property
    def potenial_popups_xpaths(self):
        return ['//div[@id="yourcx_layer"]//a[@class="yourcx_close"]',]

    @property
    def cookies_close_xpath(self):
        return './/button[contains(@id, "onetrust-accept")]'

    @property
    def store_picked_xpath(self):
        return './/ul[@class="user-navbar"]/li[@class="top-shop-details"]/a[@data-shop-name]/@data-shop-name' # noqa

    def products_discovery_map(self):
        if "new" in urlsplit(self.current_url).netloc:
            product_map = {
                    3: {
                        "product_xpath": './/div[contains(@class, "ProductBlockWrapper_wrapper")]/a[contains(@class, "ProductBlockName_name")]', # noqa
                        "product_parser": self.parse_level_3_product_element_new,
                        "product_current_page_xpath": './/div[contains(@class, "PaginationSmall")]/input[contains(@class, "PageInput")]/@value', # noqa
                        "product_next_page_button_xpath": './/div[contains(@class, "PaginationSmall")]/button[@aria-label="Strona Następna"]', # noqa
                        "product_last_page_xpath": '//div[contains(@class, "PaginationSmall")]/span[./preceding::span[contains(@class, "PaginationSmall_totalPagesTex")]]/text()', # noqa
                        "use_webelements": False,
                    },
                }
        else:
            product_map = {
                    3: {
                        "product_xpath": './/div[@class="product" and @data-product-id and @data-lm-reference]/a[@class="url "]', # noqa
                        "product_parser": self.parse_level_3_product_element,
                        "product_current_page_xpath": './/div[contains(@class, "pagination-top")]//div[@class="paging"]//span[@class="current link"]/text()', # noqa
                        "product_next_page_button_xpath": './/div[contains(@class, "pagination-top")]//div[@class="paging"]/a[contains(@class, "next") and not(contains(@class, "disabled"))]', # noqa
                        "product_last_page_xpath": './/div[contains(@class, "pagination-top")]/div[@class="paging"]/a[@class="page"][last()]/text()', # noqa
                        "use_webelements": False,
                    },
                }
        return product_map

    def parse_level_3_product_element(self, html_element):
        url = html_element.xpath('./@href')[0]
        name = html_element.xpath('.//h3[@class="title"]/text()')[0]
        product_id = html_element.xpath('.//span[@data-product-id]/@data-product-id')[0] # noqa
        return {
                "url": urljoin(self.store_url, url),
                "name": name.strip(),
                "product_id": product_id,
                }

    def parse_level_3_product_element_new(self, html_element):
        url = html_element.xpath('./@href')
        name = html_element.xpath('.//span[contains(@class, "ProductBlockName")]/text()')[0] # noqa
        product_id = self.extract_product_id_from_url(url=url)
        return {
                "url": urljoin(self.store_url, url),
                "name": name.strip(),
                "product_id": product_id,
                }

    def categories_discovery_map(self):
        # LeroyMerlin have 2 versions of site and they are redirecting slowly to new version.
        if "new" in urlsplit(self.current_url).netloc:
            category_map = {
                0: {
                    "category_xpath": './/ul[contains(@class, "MegaMenuMegaWorlds_wrapper")]//li[.//a[contains(@class, "Link_wrapper")]]/a', # noqa
                    "category_parser": self.parse_level_0_category_element,
                    "has_childs": True,
                    "has_products": False,
                    "use_webelements": False,
                    },
                1: {
                    "category_xpath": './/div[contains(@class, "MegaMenuWorldsList_masonryColumn")]//li[@class="MegaMenuWorldsItem_wrapper__FbsHv"]/a[contains(@class, "Link_wrapper")]', # noqa
                    "category_parser": self.parse_level_1_category_element,
                    "has_childs": True,
                    "has_products": False,
                    "use_webelements": False,
                    },
                2: {
                    "category_xpath": './/div[contains(@class, "CatalogListItem_wrapper")]//a[contains(@class, "CatalogListItem_nameWrapper")]', # noqa
                    "category_parser": self.parse_level_2_category_element,
                    "has_childs": True,
                    "has_products": False,
                    "use_webelements": False,
                    },
                3: {
                    "category_xpath": './/div[contains(@class, "ProductListCategories_collapseContent")]//a[contains(@class, "ProductListCategoriesItem_item") and not(contains(@class, "ProductListCategoriesItem_active"))]', # noqa
                    "category_parser": self.parse_level_3_category_element_new,
                    "has_childs": False,
                    "has_products": True,
                    "use_webelements": False,
                    },
            }
        else:
            category_map = {
                0: {
                    "category_xpath": './/div[@class="mega-menu-content"]/ul[contains(@class, "mega-world-items")]/li[contains(@class, "menu-item")]/a[@class="menu-link products"]', # noqa
                    "category_parser": self.parse_level_0_category_element,
                    "has_childs": True,
                    "has_products": False,
                    "use_webelements": False,
                    },
                1: {
                    # //nav[contains(@class, "dropdown-menu")]/div[@class="dropdown-menu-wrapper"]//ul[contains(@class, "dropdown-list")]/li[@class="dropdown-item"]/a[contains(@class, "dropdown-link")]
                    "category_xpath": '//div[@class="list"]/h2//a',
                    "category_parser": self.parse_level_1_category_element,
                    "has_childs": True,
                    "has_products": False,
                    "use_webelements": False,
                    },
                2: {
                    "category_xpath": './/div[@class="list"]/h2//a',
                    "category_parser": self.parse_level_2_category_element,
                    "has_childs": True,
                    "has_products": False,
                    "use_webelements": False,
                    },
                3: {
                    "category_xpath": './/ul[@class="menu"]/li[contains(@class, "category-item") and not(contains(@class, "active"))]/a', # noqa
                    "category_parser": self.parse_level_3_category_element,
                    "has_childs": False,
                    "has_products": True,
                    "use_webelements": False,
                    },
            }
        return category_map

    def parse_level_0_category_element(self, html_element):
        url = html_element.xpath('./@href')[0]
        name = name = html_element.text_content()
        category_id = self. extract_category_id_from_url(url=url)
        return {
            "url": urljoin(self.store_url, url),
            "name": name.strip(),
            "category_id": category_id,
            }

    def parse_level_1_category_element(self, html_element):
        url = html_element.xpath('./@href')[0]
        name = name = html_element.text_content()
        category_id = self. extract_category_id_from_url(url=url)
        return {
            "url": urljoin(self.store_url, url),
            "name": name.strip(),
            "category_id": category_id,
            }

    def parse_level_2_category_element(self, html_element):
        url = html_element.xpath('./@href')[0]
        name = html_element.text_content()
        category_id = self. extract_category_id_from_url(url=url)
        return {
            "url": urljoin(self.store_url, url),
            "name": name.strip(),
            "category_id": category_id,
            }

    def parse_level_3_category_element(self, html_element):
        url = html_element.xpath('./@href')[0]
        name = html_element.text
        category_id = self. extract_category_id_from_url(url=url)
        return {
            "url": urljoin(self.store_url, url),
            "name": name.strip(),
            "category_id": category_id,
            }

    def parse_level_3_category_element_new(self, html_element):
        url = html_element.xpath('./@href')[0]
        name = html_element.xpath('./span[@class="Link_link__Knnbf"]/span/text()')[0]
        category_id = self. extract_category_id_from_url(url=url)
        return {
            "url": urljoin(self.store_url, url),
            "name": name.strip(),
            "category_id": category_id,
            }

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