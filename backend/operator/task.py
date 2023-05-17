import importlib
from operator.base import BaseOperator


class TaskOperator(BaseOperator):
    """
    Specified Operator for processing Tasks.
    """

    def __init__(self, task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task = task

    def load_scraper(self):
        try:
            scraper_module = importlib.import_module(
                f"scraper.stores.{self.task.store.package}.{self.task.store.module_name}"
            )
            scraper = getattr(scraper_module, f'{self.task.store.scraper_class}')
            self.logger.info(f'Successfully loaded scraper object: {scraper}')
            return scraper
        except Exception as e:
            self.logger.error(f'(import_scraper) Some other excpetion: {e}')
            raise
