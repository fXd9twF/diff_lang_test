from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



def test_guest_should_see_basket(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#language_selector > div > select"))
    select.select_by_value(language)
    browser.find_element(By.CSS_SELECTOR, "#language_selector > button").click()
    cart_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form > button")))
    assert cart_button is not None, "cart_button has not been found"
