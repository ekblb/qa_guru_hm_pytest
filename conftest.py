import pytest
from selene import browser

@pytest.fixture(scope='function')
def set_browser_size():
    browser.config.window_width = 480
    browser.config.window_height = 1100

@pytest.fixture(scope='function')
def open_and_close_browser(set_browser_size):
    browser.open('https://www.ecosia.org/')
    yield
    browser.quit()
