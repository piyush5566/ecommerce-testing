from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#form-login > div.text-end > button")
    # LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ALERT_MESSAGE = (By.ID, "alert")

    def login(self, email, password, click_post_wait=8):
        self.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        sleep(12)
        self.find_element(*self.LOGIN_BUTTON).click()
        # from selenium.webdriver.common.action_chains import ActionChains
        # ActionChains(self.driver).move_to_element(
        #     self.find_element(*self.LOGIN_BUTTON)).click().perform()
        sleep(click_post_wait)
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.LOGIN_BUTTON)
        # ).click()
        # self.find_element(*self.LOGIN_BUTTON).click()
        # # Wait for button to be clickable
        # login_button = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.LOGIN_BUTTON)
        # )

        # # Scroll the button into view
        # self.driver.execute_script(
        #     "arguments[0].scrollIntoView(true);", login_button)
        # sleep(1)

        # # Try multiple click methods
        # try:
        #     # Try regular click first
        #     login_button.click()
        # except:
        #     try:
        #         # Try JavaScript click if regular click fails
        #         # self.driver.execute_script(
        #         #     "arguments[0].click();", login_button)
        # from selenium.webdriver.common.action_chains import ActionChains
        # ActionChains(self.driver).move_to_element(
        #     login_button).click().perform()
        #     except:
        #         # If both fail, try moving to element and clicking
        #         from selenium.webdriver.common.action_chains import ActionChains
        #         ActionChains(self.driver).move_to_element(
        #             login_button).click().perform()

        # sleep(10)

    def get_alert_message(self):
        return self.find_element(
            *self.ALERT_MESSAGE).text
