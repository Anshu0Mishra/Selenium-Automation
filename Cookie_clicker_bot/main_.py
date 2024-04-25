from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime


service = Service(executable_path='C:/Development/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by="id", value="cookie")
cursor = driver.find_element(by="css selector", value="#buyCursor")
grandma = driver.find_element(by="css selector", value="#buyGrandma")
factory = driver.find_element(by="css selector", value="#buyFactory")
mine = driver.find_element(by="css selector", value="#buyMine")
shipment = driver.find_element(by="css selector", value="#buyShipment")
alchemy = driver.find_element(by="id", value="buyAlchemy lab")
portal = driver.find_element(by="css selector", value="#buyPortal")
time_machine = driver.find_element(by="id", value="buyTime machine")


v_cursor = cursor.text.strip("Cursor - Autoclicks every 5 seconds.")
v_grandma = grandma.text.strip("Grandma - A nice grandma to bake more cookies.")
v_factory = factory.text.strip("Factory - Produces large quantities of cookies.")
v_mine = mine.text.strip("Mine - Mines out cookie dough and chocolate chips.")
v_shipment = shipment.text.strip("Shipment - Brings in fresh cookies from the cookie planet.")
v_alchemy = alchemy.text.strip("Alchemy lab - Turns gold into cookies!")
v_portal = portal.text.strip("Portal -  Opens a door to the Cookieverse.")
v_time_machine = time_machine.text.strip("Time machine - Brings cookies from the past, before they were even eaten.")


def money_checker(paisa):
    if paisa == v_cursor:
        cursor.click()
    elif paisa == v_grandma:
        grandma.click()
    elif paisa == v_factory:
        factory.click()
    elif paisa == v_mine:
        mine.click()
    elif paisa == v_shipment:
        shipment.click()
    elif paisa == v_alchemy:
        alchemy.click()
    elif paisa == v_portal:
        portal.click()
    elif paisa == v_time_machine:
        time_machine.click()


count = "59"
game_on = True
while game_on:
    cookie.click()
    money = driver.find_element(by="id", value="money").text
    timeout = datetime.datetime.now()  # 5 second
    current_minute = timeout.time().strftime("%M")
    if current_minute < count:
        money_checker(money)
    else:
        game_on = False
        cookie_per_sec = int(money) / 60
        print(float(cookie_per_sec))
