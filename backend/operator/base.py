from utilities.logger import logger


class BaseOperator:
    """
    Base class for other tasks.
    """

    def __init__(self):
        self.logger = logger
