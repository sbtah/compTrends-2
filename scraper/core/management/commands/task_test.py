from django.core.management.base import BaseCommand
from utilities.logger import logger
from tasker.task import Tasker
from objects.models.tasks import Task


def start_tasker():

    task = Task.objects.all().first()
    print(task.type)
    tasker = Tasker(task=task)
    scraper_class  = tasker.load_scraper()
    print(scraper_class)

    # Process Category Crawl Task
    with scraper_class(requested_url=task.url, store_url=task.store.discovery_url) as scraper:
        element = scraper.visit_page(url=scraper.requested_url)
        generator = scraper.find_categories_data(category_level=task.category_level, html_element=element)
        for cat in generator:
            # Create new task for child categories if has_childs
            # Store Category Object via API Call ?
            print(cat)



class Command(BaseCommand):
    '''Base command for restarting Celery workers.'''

    def handle(self, *args, **kwargs):
        start_tasker()