from time import sleep
import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from utils.constants import BASE_URL, VALID_CREDENTIALS, INVALID_CREDENTIALS


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_url(BASE_URL + "?route=account/login")
    login_page.login(
        VALID_CREDENTIALS['email'], VALID_CREDENTIALS['password'])
    assert "My Account" in driver.title


def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_url(BASE_URL + "?route=account/login")
    login_page.login(
        INVALID_CREDENTIALS['email'], INVALID_CREDENTIALS['password'], click_post_wait=1)

    assert "No match for E-Mail Address and/or Password." in login_page.get_alert_message()
