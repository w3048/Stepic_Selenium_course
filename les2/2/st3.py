from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    value_x1 = browser.find_element_by_id('num1').text
    value_x2 = browser.find_element_by_id('num2').text
    print(value_x1, value_x2)
    y = int(value_x1) + int(value_x2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(y))
    
    button = browser.find_element_by_css_selector('.btn.btn-default')
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()