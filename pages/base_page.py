from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def pause_execution(self, pause_time=2):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(pause_time)
