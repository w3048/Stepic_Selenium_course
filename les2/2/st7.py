from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    input_field_first_name = browser.find_element_by_css_selector('div.form-group>:nth-child(2)')
    input_field_first_name.send_keys('John')
    
    input_field_last_name = browser.find_element_by_css_selector('div.form-group>:nth-child(4)')
    input_field_last_name.send_keys('Smith')
    
    input_field_mail = browser.find_element_by_css_selector('div.form-group>:nth-child(6)')
    input_field_mail.send_keys('john@smith.com')
    
    upfile = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    upfile.send_keys(file_path)
    
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()