from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def login(email="flower_space@yahoo.com", password="prantra@7"):
    browser = webdriver.Chrome()
    browser.get("http://www.quora.com")
    time.sleep(1)

    elem = browser.find_element_by_name("email")
    elem.send_keys(email)

    elem = browser.find_element_by_name("password")
    elem.send_keys(password)

    elem.send_keys(Keys.RETURN)
    time.sleep(1)

    return browser


def sendPageDownPressEvents(browser, no_of_page_downs):
    body = browser.find_element_by_tag_name("body")
    while(no_of_page_downs>0):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)
        no_of_page_downs-=1
    time.sleep(2)
