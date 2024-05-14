import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Language for the tests"
    )

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def language(request):
    return request.config.getoption("--language")
