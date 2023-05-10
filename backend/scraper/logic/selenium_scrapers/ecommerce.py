from typing import Callable, Iterator, List, Tuple, Union, Dict
from datetime import datetime
from lxml.html import HtmlElement
from selenium.webdriver.remote.webelement import WebElement
from scraper.logic.selenium_scrapers.base import BaseSeleniumScraper


class EcommerceSeleniumScraper(BaseSeleniumScraper):
    """
    General Ecommerce scraper.
    """

    def __init__(self, requested_url, store_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.requested_url = requested_url
        self.store_url = store_url

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

    def categories_discovery_map(self) -> dict:
        """
        Dictionary that will map category structure of store.

        - :category_xpath:
            Xpath that returns list of Category HtmlElements or Webelements.
        - :category_parser:
            Callable that will extract URL and Name for Product.
        Should return dict with schema like:
        - :has_childs:
            True if Category have child Categories.
        - :has_products:
            True if Category have products to scrape.
        - :use_webelements: If set to True we will return Category elements as
            Selenium's Webelements. Otherwise we will work on HtmlElements.

        {
            "0": {
                "category_xpath": str,
                "category_parser": callable,
                "has_childs": bool,
                "has_products": bool,
                "use_webelements": bool,
            },
        }

        Where Keys 0 - 2 implies Category level.
        """
        raise NotImplementedError

    def products_discovery_map(self) -> dict:
        """
        Dictionary that will map product structure of store on Category page.
        If for instance Category of level 0 have products,
        then we define product_xpath that leads to Product element.

        - :product_xpath:
            Xpath that returns list of Product HtmlElements or Webelements.
        - :product_parser:
            Callable that will extract URL and Name for Product.
        Should return dict with schema like:
        {
            "0": {
                "product_xpath": str,
                "product_parser": callable,
            },
        }
        Where Keys 0 - 2 implies Category level.
        """
        raise NotImplementedError

    def visit_page(self, url: str) -> HtmlElement:
        """
        Entrypoint for all scraping logic.
        Visits requested page by url.
        Since we don't store session or cookies,
        each time with have to close cookies banner.
        Returns HtmlElement generated after banner was closed.
        """
        try:
            request = self.selenium_get(url=url)
            if request is not None:
                element = self.generate_html_element()
                self.close_cookies_banner(html_element=element)
                after_element = self.generate_html_element()
                return after_element
            else:
                self.logger.error("Failed at requesting page URL.")
                raise ValueError
        except Exception as e:
            self.logger.error(f"(visit_page) Some other Exception: {e}")
            raise

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
            self.logger.error(
                f"(close_cookies_banner) Some other Exception: {e}"
            )

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
                self.random_sleep_small()
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

    def find_category_data(
            self,
            category_level: int,
            html_element: HtmlElement,
        ) -> Union[Iterator[Dict], None]:
        """
        Looks for Category Elements in given HtmlElement.
        Return generator of tuples with URL/Name of Categories.

        - :arg category_level:
            Level of Category, used to get data from categories_map.
        - :arg html_element: Lxml HtmlElement to process.
        """
        self.logger.info(f"Discovery process for Categories of level: {category_level} started.") # noqa
        # Get category map.
        categories_map = self.categories_discovery_map()
        # Get list of Webelements or HtmlElements.
        elements_type = categories_map[f"{category_level}"]["use_webelements"]
        if elements_type == True:
            # Using Webelements.
            self.logger.info('Looking for Webelements for Categories.')
            categories_list = self.find_selenium_elements(
                # categories_map[f'{category_level}']["category_xpath"]
                xpath_to_search=categories_map[f'{category_level}']["category_xpath"], # noqa
            )
        elif elements_type == False:
            # Or HtmlElements.
            self.logger.info('Looking for HtmlElements for Categories.')
            categories_list = self.find_all_elements(
                    html_element=html_element,
                    xpath_to_search=categories_map[f'{category_level}']["category_xpath"], # noqa
                )
        else:
            self.logger.error(
                "(find_category_data) Error while getting 'use_webelements'. Quiting." # noqa
            )
            raise ValueError
        if categories_list:
            self.logger.info(
                f"Successfully found: {len(categories_list)} Categories elements. Processing."
            )
            return self.prepare_category_discovery_data(
                list_of_elements=categories_list,
                custom_parser=categories_map[f'{category_level}']["category_parser"], # noqa
                has_childs=categories_map[f'{category_level}']["has_childs"],
                has_products=categories_map[f'{category_level}']["has_products"], # noqa
            )
        else:
            self.logger.error(
                f"Searching for Category elements failed. Quiting."
            )
            self.make_screenshot()
            raise ValueError

    # TODO
    # SOME IDEA...
    def prepare_category_discovery_data(
            self,
            list_of_elements: List[Union[WebElement, HtmlElement]],
            custom_parser: Callable,
            has_childs: bool,
            has_products: bool,
        ) -> Union[Iterator[Dict], None]:
        """
        Takes list of HtmlElements or Webelements
        and returns generator of dictionaries with prepared data containing:
            urls, names, has_childs, has_products for Category.

        - :arg list_of_elements:
            List of HtmlElements or Selenium Webelement to process.
        - :arg custom_parser:
            Method that will be used to extract URL/Name,
            from single given element.
            Should return dict with,
            "url": value_for_url, "name": value_for_name.
        - :arg has_childs: True or False, should be set in:
            categories_discovery_map property.
        - :arg has_products: True or False, should be set in:
            categories_discovery_map property.
        """
        if isinstance(list_of_elements, list):
            assert len(list_of_elements) > 0, "Received an empty list, Nothing to extract." # noqa
            try:
                return ({**custom_parser(element), "has_childs":has_childs, "has_products": has_products} for element in list_of_elements) # noqa
            except Exception as e:
                self.logger.error(
                    f"(prepare_category_discovery_data) Some other exception: {e}"
                )
                return None
        else:
            self.logger.error(
                f"(prepare_category_discovery_data) Argument received for list of elements should be of type list. Received: {type(list_of_elements)}" # noqa
            )
            raise TypeError

    def find_products_data(
            self,
            category_level: int,
            html_element: HtmlElement,
        ) -> Union[Iterator[Tuple[str, str]], None]:
        """"""
        pass

    def find_product_pages_for_all_pages_selenium(
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
                current_page_number_from_xpath = self.find_element(
                    html_element=element,
                    # Current page Xpath
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



#     def extract_urls_with_names(
#             self,
#             list_of_elements: list,
#             custom_parser: Callable,
#         ) -> Union[Iterator[Tuple[str, str]], None]:
#         """
#         Takes list of HtmlElements or Webelements
#         and returns generator of tuples with urls and names.
#  
#         - :arg list_of_elements:
#             List of HtmlElements or Selenium Webelement to process.
#         - :arg custom_parser:
#             Method that will be used to extract URL/Name
#             from single given element.
#             Should return dict with "url": value, "name": value.
#         """
#         if isinstance(list_of_elements, list):
#             assert len(list_of_elements) > 0, "Received an empty list, Nothing to extract." # noqa
#             try:
#                 return (custom_parser(element) for element in list_of_elements)
#             except Exception as e:
#                 self.logger.error(
#                     f"(extract_urls_with_names) Some other exception: {e}"
#                 )
#                 return None
#         else:
#             self.logger.error(
#                 f"(extract_urls_with_names) Argument received should be list. Received: {type(list_of_elements)}" # noqa
#             )
#             raise TypeError