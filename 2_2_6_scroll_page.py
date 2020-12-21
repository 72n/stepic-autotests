from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_id('input_value').text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f'{calc(x)}')

    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()

    input2 = browser.find_element_by_id("robotsRule")
    input2.click()


    # Отправляем заполненную форму
    # button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
