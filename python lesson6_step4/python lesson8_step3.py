from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id("num1")
    #value = x_element.get_attribute("valuex")
    x = x_element.text
    x = int(x)

    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    y = int(y)
    z = x+y
    z = str(z)
    print(z)
    option1 = browser.find_element_by_id("dropdown")
    option1.click()
    time.sleep(1)

    option2 = browser.find_element_by_css_selector(f"[value='{z}']").click()
    time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

