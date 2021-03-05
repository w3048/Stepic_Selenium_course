from selenium import webdriver
import math
import time

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    value_x = browser.find_element_by_id('input_value').text
    y = math.log(abs(12 * math.sin(int(value_x))))

    input_y = browser.find_element_by_id('answer')
    input_y.send_keys(str(y))
    
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer = alert_text.split(': ')[-1]
    print(answer)
    
finally:
    time.sleep(60)
    browser.quit()