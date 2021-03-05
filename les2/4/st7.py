from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    waiting = WebDriverWait(browser, 30).until(
            EC.text_to_be_present_in_element((By.ID,'price'),'$100')
        )
    button = browser.find_element_by_id('book')
    button.click()
    
    value_x = browser.find_element_by_id('input_value').text
    y = math.log(abs(12 * math.sin(int(value_x))))

    input_y = browser.find_element_by_id('answer')
    input_y.send_keys(str(y))
    
    button_send = browser.find_element_by_id('solve')
    button_send.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer = alert_text.split(': ')[-1]
    print(answer)
    
finally:
    time.sleep(10)
    browser.quit()