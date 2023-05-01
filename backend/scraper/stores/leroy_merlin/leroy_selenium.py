from scraper.logic.selenium_scrapers.ecommerce import EcommerceSeleniumScraper


class LeroyMerlinSeleniumScraper(EcommerceSeleniumScraper):
    """
    Scraper for Leroy Merlin store.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def potenial_popups_xpaths(self):
        raise NotImplementedError

    @property
    def cookies_close_xpath(self):
        return './/button[contains(@id, "onetrust-accept")]'

    @property
    def store_picked_xpath(self):
        return './/ul[@class="user-navbar"]/li[@class="top-shop-details"]/a[@data-shop-name]/@data-shop-name'

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
