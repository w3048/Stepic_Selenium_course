from selenium import webdriver
import math
import time

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    value_x = browser.find_element_by_id('treasure')
    x = value_x.get_attribute('valuex')
    print(x)
    y = math.log(abs(12 * math.sin(int(x))))

    input_y = browser.find_element_by_id('answer')
    input_y.send_keys(str(y))
    
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[value='robots']")
    radiobutton.click()   
    
    button = browser.find_element_by_css_selector('btn.btn-default')
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()