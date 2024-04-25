from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/Development/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.instagram.com/")
ACCOUNT_TO_GET = "davidbombal"
USERNAME = os.environ.get("USERNAME")
PASSCODE = os.environ.get("PASSCODE")
time.sleep(5)
user = driver.find_element(by="name", value="username")
user.send_keys(USERNAME)
pass_insta = driver.find_element(by="name", value="password")
time.sleep(2)
pass_insta.send_keys(PASSCODE)
time.sleep(2)
log_in = driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[3]/button/div')
log_in.click()
time.sleep(10)
not_now = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div')
not_now.click()
time.sleep(5)
not_now_2 = driver.find_element(by="xpath", value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/'
                                                  'div/div/div[3]/button[2]')
not_now_2.click()
time.sleep(5)

search_button = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div')
search_button.click()

time.sleep(5)

search_input = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
search_input.send_keys('Person to Search')

time.sleep(5)

Person_name = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
Person_name.send_keys(Keys.ENTER)

time.sleep(2)

click_on_first = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/'
                                                       'div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/'
                                                       'div[1]/div/div/div[2]/div/div/span/span')
click_on_first.send_keys(Keys.ENTER)

driver.close()
