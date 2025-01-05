import os
import sys

import pytest

from utils.driver_setup import get_driver

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()
