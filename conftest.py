import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as F_Options


def webdriver_chrome_browser(user_language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    return browser

def webdriver_firefox_browser(user_language):
    options = F_Options()
    options.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(options=options)
    return browser

supported_browsers = {
    'chrome': webdriver_chrome_browser,
    'firefox': webdriver_firefox_browser
}

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        help='Choose browser: chrome or firefox'
    )
    parser.addoption(
        '--language', action='store', default='ru',
        help='Choose language: ru, en, es, etc.'
    )

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name in supported_browsers:
        browser = supported_browsers[browser_name](user_language)
        print(f'\nStart browser {browser_name} for test..')
    else:
        raise pytest.UsageError(
            f'{browser_name} not supported! '
            f'Supported browsers: {supported_browsers.keys()}'
        )
    yield browser
    print('\nQuit browser..')
    browser.quit()