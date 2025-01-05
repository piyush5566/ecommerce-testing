from selenium import webdriver
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--enable-logging --v=1')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

