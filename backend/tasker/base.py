from utilities.logger import logger


class BaseTasker:
    """
    Base class for other tasks.
    """

    def __init__(self):
        self.logger = logger
