from pages.cart_page import CartPage
from utils.constants import BASE_URL


def test_add_to_cart(setup):
    driver = setup
    cart_page = CartPage(driver)
    cart_page.open_url(BASE_URL)
    cart_page.add_to_cart()
    items_count = cart_page.get_cart_items_count()
    assert items_count == 1


def test_cart_total_price(setup):
    driver = setup
    cart_page = CartPage(driver)
    cart_page.open_url(BASE_URL)
    cart_page.add_to_cart()
    total_price = cart_page.get_total_price()
    assert total_price == "$602.00"  # Adjust based on product price.
