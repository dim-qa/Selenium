import pytest
from selenium import webdriver

"""Фикстура настраивает запуск браузера"""


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
