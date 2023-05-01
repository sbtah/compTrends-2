import time
from typing import List, Union, Iterator, Callable, Tuple
from scraper.helpers.randoms import (
    random_sleep_medium,
    random_sleep_small,
    random_sleep_long,
)
from lxml.html import HtmlElement
from scraper.logic.selenium_scrapers.base import BaseSeleniumScraper


class EcommerceSeleniumScraper(BaseSeleniumScraper):
    """
    General Ecommerce scraper.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def potenial_popups_xpaths(self) -> List[str]:
        """
        Should return a list of Xpaths to can appear on the Website randomly.
        """
        raise NotImplementedError

    @property
    def cookies_close_xpath(self) -> str:
        """Xpath to element that closes cookies policy banner on click."""
        raise NotImplementedError

    @property
    def store_picked_xpath(self) -> str:
        """
        Xpath to element that will return text value,
        for currently picked Local Store.
        """
        raise NotImplementedError

    def close_cookies_banner(self, html_element: HtmlElement) -> None:
        """
        Finds Cookies Policy in provided HtmlElement and closes it.
        Needs self.cookies_close_xpath to work.
        """
        try:
            self.find_and_click_selenium_element(
                html_element=html_element,
                xpath_to_search=self.cookies_close_xpath,
            )
            self.logger.info("Successfully closed cookies policy banner.")
        except Exception as e:
            self.logger.error(f"(close_cookies_banner) Some other Exception")

    def close_popups_elements_on_error(self) -> None:
        """
        Searches list of knows Xpathses for popup elements.
        If element is found, closes it.
        """
        for xpath in self.potenial_popups_xpaths:
            element = self.find_selenium_element(
                xpath_to_search=xpath, ignore_not_found_errors=True
            )
            if element is not None:
                self.logger.info("Found critical popup element. Closing.")
                self.move_and_click(selenium_element=element)
                random_sleep_small()
            else:
                pass

    def get_current_store(self, html_element: HtmlElement) -> str:
        """
        Returns text value for currently picked Local Store.

        - :arg html_element: Lxml HtmlElement to process.
        """
        try:
            store = self.find_element(
                html_element=html_element,
                xpath_to_search=self.store_picked_xpath,
            )
            self.logger.info(
                    f"Successfully returned a store element: {store}"
            )
            return store
        except Exception as e:
            self.logger.error(f"(get_current_store) Some other Exception: {e}")
            raise

    def validate_store_picked(self, store_name: str ) -> Union[True, False]:
        """
        Validates value of chosen store,
        with current value of Local Store on site.
        Returns True on success.
        """
        element = self.generate_html_element()
        current_store = self.get_current_store(html_element=element)
        if current_store:
            if current_store == store_name:
                self.logger.info(
                    f"Validation of Local Store successfull: Current Store:{current_store} ; Chosen Store: {store_name}" # noqa
                )
                return True
            else:
                return False
        else:
            self.logger.error(
                '(validate_store_picked) Failed at getting Store name value'
            )
            raise AttributeError

    def pick_local_store_by_name(
            self,
            store_name: str,
            html_element: HtmlElement
        ) -> Union[True, False]:
        """
        Searches for element that is used to pick local store.
        Properly pick local store.
        Should return True on success and False on fail.
        Needs to be implemented on specific store SeleniumScraper level.

        - :arg store_name: string representing Local Store name.
        - :arg html_element: Lxml HtmlElement to process.
        """
        raise NotImplementedError

    def extract_urls_with_names(
            self,
            list_of_elements: list,
            custom_parser: Callable
        ) -> Union[Iterator[Tuple], None]:
        """
        Takes list of HtmlElements or Webelements
        and returns generator of tuples with urls and names.

        - :arg list_of_elements:
        """
        if isinstance(list_of_elements, list):
            assert len(list_of_elements) > 0, "Received an empty list, Nothing to extract." # noqa
            try:
                return (custom_parser(element) for element in list_of_elements)
            except Exception as e:
                self.logger.error(f"(extract_urls_with_names) Some other exception.")
                return None
        else:
            self.logger.error(
                f"(extract_urls_with_names) Argument received should be list. Received: {type(list_of_elements)}" # noqa
            )
            raise TypeError

    def extract_urls_with_names_old(
        self,
        html_element,
        xpath_to_search,
        parser_used=None,
        extract_with_selenium=False,
    ):
        """
        Used in discovery of WebPages Elements on current page.
        Finds all Urls and 'Names' in given HtmlElements.
        Returns generator of tuples, containing (url, name).
        :param xpath_to_search: - Xpath that should return list of HtmlElements
            or SeleniumWebElements.
        :param parser_used: - class method that will extract needed data,
            (URL, Name) from each element in list.
        :param extract_with_selenium: - Default to False means,
            that parsing will expect to work on HtmlElements, while True means,
            that parser have to deal with Selenium Web Element.
        """
        if extract_with_selenium == False:
            categories_list = self.find_all_elements(
                html_element=html_element,
                xpath_to_search=xpath_to_search,
            )
        else:
            categories_list = self.find_selenium_elements(
                xpath_to_search=xpath_to_search,
            )

        if categories_list:
            self.logger.info(
                f"URLS/Names list created, returned {len(categories_list)} elements."  # noqa
            )
            if extract_with_selenium == False:
                return (
                    parser_used(HtmlElement=x, SeleniumWebElement=None)
                    for x in categories_list
                )
            else:
                return (
                    parser_used(SeleniumWebElement=x, HtmlElement=None)
                    for x in categories_list
                )
        else:
            self.logger.info(f"Failed loading URLS/Names list from HTML,")
            return None

    def find_all_category_pages(
        self,
        html_element,
        category_level=1,
        parser_used=None,
        extract_with_selenium=False,
    ):
        """
        Given then HtmlElement.
        Return generator of tuples for CategoryPage: (url, name).
        self.categories_discovery_xpath_dict have to be configured,
            with CategoryPage related xpathses.
        self.categories_discovery_xpath_dict keys are implying CategoryPage level,
            where Root/Main CategoryPage is 1 while childs are 2, 3, 4 and so on.
        :param parser_used:
        :param extract_with_selenium:
            - If set to true data will be extracted with Selenium,
                instead of lxml.
        """
        if (
            self.categories_discovery_xpath_dict.get(category_level)
            and parser_used is not None
        ):
            categories = self.extract_urls_with_names(
                html_element=html_element,
                xpath_to_search=self.categories_discovery_xpath_dict[category_level][
                    "category_element_xpath"
                ],
                parser_used=parser_used,
                extract_with_selenium=extract_with_selenium,
            )
            return categories
        else:
            self.logger.error(
                "(find_all_category_pages) Missing critical Xpathses or CategoryPage parser. Quiting."
            )
            self.do_cleanup()
            return None

    def find_all_product_elements(
        self,
        html_element,
        category_level=1,
        parser_used=None,
        extract_with_selenium=False,
    ):
        """
        Given then HtmlElement.
        Return generator of tuples for ProductPage: (url, name).
        self.products_discovery_xpath_dict have to be configured,
            with ProductPage related xpathses.
        Sometimes products can be displayed differently on different CategoryPage.
        :param category_level: is used here to link ProductPages Xpathses with proper category.
        For instance: If child category (level=2) is displaying product data, then we fetch
            self.products_discovery_xpath_dict for key '2' in dictionary of Xpathses.
        :param extract_with_selenium:
            - If set to true data will be extracted with Selenium,
                instead of lxml.
        """
        if (
            self.products_discovery_xpath_dict.get(category_level)
            and parser_used is not None
        ):
            products = self.extract_urls_with_names(
                html_element=html_element,
                xpath_to_search=self.products_discovery_xpath_dict[category_level][
                    "product_url_xpath"
                ],
                parser_used=parser_used,
                extract_with_selenium=extract_with_selenium,
            )
            return products
        else:
            self.logger.error(
                "(find_all_product_pages) Missing critical Xpathses or ProductPage parser. Quiting."
            )
            self.do_cleanup()
            return None

    def find_product_elements_for_all_pages_selenium(
        self, category_level=1, parser_used=None, extract_with_selenium=False
    ):
        """
        Parses all products for all pages on specified ProductPage.
        Relies on Selenium since it's only clicking next page button.
        To work you need to configure:
        self.products_discovery_xpath_dict
        Returns a generator of tuples with ProductPage data: (url, name).
        """
        if parser_used is not None:
            current_page = 1
            element = self.generate_html_element()
            current_page_number_from_xpath = self.find_all_elements(
                html_element=element,
                # Current page Xpath
                xpath_to_search=self.products_discovery_xpath_dict[category_level]["product_current_page_xpath"],
                ignore_not_found_errors=True,
            )
            self.logger.info(
                f"Current page; XPath: {current_page_number_from_xpath[0].text_content().strip() if current_page_number_from_xpath != None else 1} Counted: {current_page}"
            )

            products = self.find_all_product_pages(
                html_element=element,
                category_level=category_level,
                parser_used=parser_used,
                extract_with_selenium=extract_with_selenium,
            )

            if products is not None:
                for prod in products:
                    yield prod
            else:
                self.logger.error(
                    f"(find_all_product_pages) Returned: '{products}' Products at URL: {self.url} - Quiting."
                )
                pass

            next_page_button = self.find_selenium_element(
                # Next Page Xpath
                xpath_to_search=self.products_discovery_xpath_dict[category_level][
                    "product_next_page_button_xpath"
                ],
                ignore_not_found_errors=True,
            )
            while next_page_button is not None:

                self.logger.info(f"Found another product page, proceeding.")
                self.initialize_html_element(next_page_button)
                next_page_button = self.find_selenium_element(
                    # Next Page Xpath
                    xpath_to_search=self.products_discovery_xpath_dict[category_level][
                        "product_next_page_button_xpath"
                    ],
                    ignore_not_found_errors=True,
                )

                current_page += 1
                new_element = self.parse_driver_response()
                current_page_number_from_xpath = self.find_all_elements(
                    html_element=new_element,
                    # Current Page Xpath
                    xpath_to_search=self.products_discovery_xpath_dict[category_level][
                        "product_current_page_xpath"
                    ],
                    ignore_not_found_errors=True,
                )
                self.logger.info(
                    f"Current page; XPath: {current_page_number_from_xpath[0].text_content().strip() if current_page_number_from_xpath != None else 1} Counted: {current_page}"
                )

                products = self.find_all_product_pages(
                    html_element=element,
                    category_level=category_level,
                    parser_used=parser_used,
                    extract_with_selenium=extract_with_selenium,
                )
                if products is not None:
                    for prod in products:
                        yield prod
                else:
                    self.logger.error(
                        f"(find_all_product_pages) Returned: '{products}' Products at URL: {self.url} - Quiting."
                    )
                    pass

            else:
                self.logger.info(
                    "Next page element not found. Parsing products - finished."
                )
        else:
            self.logger.error("Missing ProductPage parser - Quiting.")
            self.do_cleanup()



    @property
    def categories_discovery_xpath_dict(self):
        """
        Dictionary of needed Xpaths and settings for discoverying CategoryPages.
        CategoryPages can have other Categories as a childs.
        Main (root) Categories are mapped to 1 while childs are 2, 3, 4 and so on.
        - :param category_element_xpath: Must return list of Elements to parse.
        return {
            1: {
                "category_element_xpath": None,
            },
        }
        """
        raise NotImplementedError

    @property
    def products_discovery_xpath_dict(self):
        """
        Dictionary of needed Xpaths and settings for discoverying ProductPages.
        ProductsPages are mapped to CategoryPage level by key.
        - :param product_url_xpath: Must return list of Elements to parse.
        return {
            1: {
                "product_url_xpath": "",
                "product_next_page_button_xpath": "",
                "product_current_page_xpath": "",
                "product_last_page_xpath": "",
                "product_previous_page_xpath": "",
            },
        }
        """
        raise NotImplementedError