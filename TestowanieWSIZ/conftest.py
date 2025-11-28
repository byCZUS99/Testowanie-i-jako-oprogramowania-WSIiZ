# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://wsiz.edu.pl/"

@pytest.fixture(scope="function")
def wsiz_home():
    options = Options()

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Wchodzimy na stronę
    driver.get(BASE_URL)

    yield driver
    driver.quit()
