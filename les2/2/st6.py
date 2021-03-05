from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from math import log, sin

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id('input_value').text
    
    x
    
    print(x)
    
    y = log(abs(12 * sin(int(x))))
    
    print(y)
    
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(y))
    
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    
    radiobutton = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
        
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()