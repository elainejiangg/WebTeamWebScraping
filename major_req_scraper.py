import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://catalog.mit.edu/degree-charts/")

major_to_courses = {}
course_to_majors = {}

majors = driver.find_elements(By.TAG_NAME, "a")

# loop through majors
for major in majors:
    try:
        link = major.get_attribute("href")
        driver.implicitly_wait(10)
        link.click()
    except:
        continue
    
    # get major name and courses
    name = driver.find_element(By.CLASS_NAME, "page-title")
    potential = driver.find_elements(By.TAG_NAME, "tr") # first one is invalid

    # only keep valid courses
    courses = []
    for course in potential:
        temp = course.find_element(By.TAG_NAME, "span")
        temp = temp.get_attribute("class")
        if "courselistcomment" in temp:
            continue
        else:
            course_name = course.find_elements(By.TAG_NAME,"td")[1].text # second one
            courses.append(course_name)
    
    major_to_courses[name] = courses

    driver.back()


    for major in major_to_courses:
        for course in major_to_courses[major]:
            if course in course_to_majors:
                course_to_majors[course].append(major)
            else:
                course_to_majors[course] = major


