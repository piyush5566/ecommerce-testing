from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[title="Add to Cart"]')
    TOTAL_CART_ITEMS_AND_PRICE = (
        By.CSS_SELECTOR, "#header-cart > div > button")

    def add_to_cart(self, product_index=0):
        sleep(8)
        add_to_cart_buttons = self.find_elements(*self.ADD_TO_CART_BUTTON)
        # print([button.get_attribute('outerHTML')
        #       for button in add_to_cart_buttons])
        # self.find_elements(*self.ADD_TO_CART_BUTTON)[product_index].click()
        add_to_cart_buttons[product_index].click()
        sleep(10)

    def get_cart_items_count(self):
        return int(self.find_element(*self.TOTAL_CART_ITEMS_AND_PRICE).text.strip().split(' ')[0])

    def get_total_price(self):
        return self.find_element(*self.TOTAL_CART_ITEMS_AND_PRICE).text.strip().split(' ')[-1]
