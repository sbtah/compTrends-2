"""
Used for local testing.
"""
import time
from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper



scraper = LeroyMerlinScraper(
    requested_url="https://www.leroymerlin.pl/relaks-w-ogrodzie/camping-biwak,a2434.html",
    store_url="https://www.leroymerlin.pl/"
)

element = scraper.visit_page(url=scraper.requested_url)
# scraper.pick_local_store_by_name()
genex = scraper.find_category_elements(category_level=3, html_element=element)
for cat in genex:
    print(cat)
scraper.quit_and_clean()