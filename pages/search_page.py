from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BAR = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > button")
    RESULTS = (By.CLASS_NAME, "product-thumb")

    def search_product(self, product_name):
        sleep(5)
        self.find_element(*self.SEARCH_BAR).send_keys(product_name)
        self.find_element(*self.SEARCH_BUTTON).click()
        sleep(5)

    def get_results(self):
        return self.find_elements(*self.RESULTS)
