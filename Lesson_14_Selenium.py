from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Opera()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id("book")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button1 = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button.click()
assert True

input1 = browser.find_element_by_id("input_value")
x = input1.text
print(x)
y = calc(x)
print(y)

input2 = browser.find_element_by_name("text")
input2.send_keys(y)

input3 = browser.find_element_by_id('solve')
input3.click()


