from utilities.logger import logger
from categories.models import Category


def api_update_or_create_category(
    parrent_eccomerce_store,
    name,
    url,
    api_url,
    scraped_id,
    category_level,
    last_scrape,
):
    """Update or create Category object with data from API call."""
    try:
        category = Category.objects.get(scraped_id=scraped_id)

        category.name = name
        category.url = url
        category.api_url = api_url
        category.category_level = category_level
        category.last_scrape = last_scrape
        category.parrent_store = parrent_eccomerce_store
        category.save()
        logger.info(f"Updated Category: {category}")
    except Category.DoesNotExist:
        category = Category.objects.create(
            name=name,
            url=url,
            api_url=api_url,
            scraped_id=scraped_id,
            category_level=category_level,
            parrent_store=parrent_eccomerce_store,
            last_scrape=last_scrape,
        )
        logger.info(f"Created Category: {category}")
    return category