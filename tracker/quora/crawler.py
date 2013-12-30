from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from utils import login
from quespageparser import prepareQuesAnsObject

driver = login()

def get_all_question_links(browser):
    question_elements = browser.find_elements_by_class_name("question_link")
    question_links = [elem.get_attribute("href") for elem in
            question_elements]
    return question_links

body = driver.find_element_by_tag_name("body")
no_of_page_downs = 20

while(no_of_page_downs>0):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_page_downs-=1

time.sleep(2)
questions = get_all_question_links(driver)

driver.quit()

print "Total Questions: %d"%(len(questions))

for link in questions:
    QA = prepareQuesAnsObject(link)
    print QA.question.text
    print len(QA.answers)


