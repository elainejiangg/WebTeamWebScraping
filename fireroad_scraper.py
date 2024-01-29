import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://fireroad-dev.mit.edu/requirements/edit/major1")

courses_to_major = []
major_to_courses = []

# id, title, date, metadata {}
id = uuid.uuid4()

# click on major on sidebar
major_count = 1
try:
    menu = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/ul[1]")
except:
    menu = driver.find_element(By.CLASS_NAME, "sub-menu collapse in")

try:
    majors = menu.find_elements(By.TAG_NAME, "li")
except:
    print("majors not found")

# current major to look at
major = majors[major_count]

# find and click on link
link = major.find_element(By.TAG_NAME, "a")
link.click()

# extract text from box
# try:
#     box = driver.find_element(By.CLASS_NAME, "card hoverable editor-card")
# except:
#     try:
#         box = driver.find_element(By.CLASS_NAME, "row edit-head")
#     except:
#         print("box not found")

# try:
#     text = box.find_element(By.TAG_NAME, "textarea").text
# except:
#     try:
#         text = box.find_element(By.ID, "contents").text
#     except:
#         print("text not found")

# extract courses from edit preview
box = driver.find_element(By.CLASS_NAME, "content")
time.sleep(10)
try:
    preview = box.find_element(By.ID, "preview-button")
    time.sleep(10)
except:
    try:
        preview = box.find_element(By.CLASS_NAME, "col s8 red-text text-darken-4")
        time.sleep(10)
    except:
        preview = box.find_element(By.TAG_NAME, "a")
        time.sleep(10)
preview.click()
time.sleep(10)

# get courses
try:
    course_ids = driver.find_elements(By.CLASS_NAME, "course-id")
    time.sleep(10)
    course_nums = []
    for number in course_ids:
        course_nums.append(number.text)
    course_names = driver.find_elements(By.CLASS_NAME, "course-title")
    time.sleep(10)
    course_titles = []
    for title in course_names:
        course_titles.append(title.text)
except:
    try:
        courses = driver.find_elements(By.CLASS_NAME, "course-tile-outer")
        time.sleep(10)
        temp_courses1 = []
        temp_courses2 = []
        for course in courses:
            ids = course.find_element(By.CLASS_NAME, "course-id").text
            time.sleep(10)
            titles = course.find_element(By.CLASS_NAME, "course-title").text
            time.sleep(10)
            temp_courses1.append(ids)
            temp_courses2.append(titles)
        course_nums = temp_courses1
        course_titles = temp_courses2
    except:
        print("courses not found")
    
print(course_nums)
print(course_titles)


        







