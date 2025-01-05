from pages.search_page import SearchPage
from utils.constants import BASE_URL


def test_product_search(setup):
    driver = setup
    search_page = SearchPage(driver)
    search_page.open_url(BASE_URL)
    search_page.search_product("Phone")
    results = search_page.get_results()
    assert len(results) > 0
    assert "Phone" in ' '.join([result.text for result in results])
