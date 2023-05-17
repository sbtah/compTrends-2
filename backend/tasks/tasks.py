import time

from celery import shared_task
from objects.models.stores import EcommerceStore
from objects.models.tasks import Task
from utilities.logger import logger


# TODO:
# Delete aftert testing.
@shared_task(name='initial_discovery_task')
def initial_discovery():
    from scraper.stores.leroy_merlin.leroy_merlin import LeroyMerlinScraper
    with LeroyMerlinScraper(
            requested_url="https://www.new.leroymerlin.pl/",
            store_url="https://www.leroymerlin.pl/"
        ) as scraper:
        element = scraper.visit_page(url=scraper.requested_url)
        generator = scraper.find_categories_data(category_level=0, html_element=element)
        for cat in generator:
            print(cat)
        scraper.quit_and_clean()


@shared_task(
        bind=True,
        autoretry_for=(Exception,),
        retry_backoff=60,
        name='create_initial_discovery_tasks',
    )
def create_initial_discovery_tasks(self):
    active_stores = EcommerceStore.objects.filter(is_active=True)
    for store in active_stores:
        created = int(time.time())
        try:
            task = Task.objects.create(
                store=store,
                url=store.discovery_url,
                type='CATEGORIES-CRAWL',
                category_level=0,
                created=created
                )
            logger.info(f'Successfully Created Task with ID: {task.id}')
        except Exception as e:
            logger.error(f'(create_initial_discovery_tasks) Exception: {e}')
