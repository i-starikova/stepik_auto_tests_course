from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    number = browser.find_element(By.CSS_SELECTOR, "img")
    get_number = number.get_attribute("valuex")
    y = calc(get_number)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()
    check_rule = browser.find_element(By.ID, "robotsRule")
    check_rule.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()