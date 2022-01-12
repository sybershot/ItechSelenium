from page_objects.yandex_search_page import YandexSearch


def search_and_validate(page_object: YandexSearch, keys):
    """
    Searches the keyword and validates that all results have expected keyword in them.
    :param page_object: YandexSearch object
    :param keys: Keyword to validate
    :return:
    """

    po = page_object
    po.go_to_home_page()
    po.search(keys)
    po.wait_for_search_results()
    po.validate(keys)
