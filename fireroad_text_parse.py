import calendar
import datetime
import json
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://fireroad-dev.mit.edu/requirements/edit/major1")


major_count = 0
menu = driver.find_element(By.ID, "majors")
time.sleep(10)

majors = menu.find_elements(By.TAG_NAME, "li")
time.sleep(10)

print(len(majors)) # 75 majors

# current major to look at
total_count = len(majors)
major = majors[0]

# while major_count < total_count:
try:
    inner_sidebar = major.find_element(By.TAG_NAME, "a")
    name = inner_sidebar.text
    time.sleep(10)
    print("major name: ", name)
except:
    try:
        inner_sidebar = major.find_element(By.TAG_NAME, "strong")
        name = inner_sidebar.text
        time.sleep(10)
        print("major name: ", name)
    except:
        print("no name found")

# find and click on link
try:
    # link = major.find_element(By.TAG_NAME, "a")
    # time.sleep(10)
    inner_sidebar.click()
    print("major clicked")
    time.sleep(10)
except:
    print("link not found")


# extract text from box
try:
    box = driver.find_element(By.CLASS_NAME, "card hoverable editor-card")
except:
    try:
        box = driver.find_element(By.CLASS_NAME, "row edit-head")
    except:
        print("box not found")

try:
    text = box.find_element(By.TAG_NAME, "textarea").text
except:
    try:
        text = box.find_element(By.ID, "contents").text
    except:
        print("text not found")

# parse text



