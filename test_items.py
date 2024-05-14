import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(buttons) > 0, 'Кнопка "Добавить в корзину" не найдена'
    assert len(buttons) < 2, 'Найдено больше одной кнопки'