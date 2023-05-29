import importlib
from tasker.base import BaseTasker


class Tasker(BaseTasker):
    """
    Specified Tasker for processing Tasks.
    """

    def __init__(self, task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task = task

    def load_scraper(self):
        try:
            scraper_module = importlib.import_module(
                f"scraper.stores.{self.task.store.package_name}.{self.task.store.module_name}" # noqa
            )
            scraper = getattr(scraper_module, f'{self.task.store.class_name}')
            self.logger.info(f'Successfully loaded scraper object: {scraper}')
            return scraper
        except Exception as e:
            self.logger.error(f'(import_scraper) Some other excpetion: {e}')
            raise

    def identify_task_type(self):
        ''''''
        pass

    def process_crawl_category(self):
        ''''''
        pass
