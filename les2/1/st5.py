from selenium import webdriver
import math
import time


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
  
try:  
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_form = browser.find_element_by_id('answer')
    input_form.send_keys(str(y)) 

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[value='robots']")
    radiobutton.click()    
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
