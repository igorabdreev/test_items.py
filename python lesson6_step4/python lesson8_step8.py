from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")

    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("Petrov")

    input1 = browser.find_element_by_name("email")
    input1.send_keys("Petrov@gmail.ru")

    #Отправляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    #Скролим страницу вниз
    browser.execute_script("window.scrollBy(0, 150);")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()