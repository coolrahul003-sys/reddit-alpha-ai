import logging

from .config import settings


def setup_logger():
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    return logging.getLogger("reddit-alpha-ai")


logger = setup_logger()
