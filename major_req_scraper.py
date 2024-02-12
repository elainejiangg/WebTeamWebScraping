import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://catalog.mit.edu/degree-charts/")

major_to_courses = {}
course_to_majors = {}

container = driver.find_element(By.ID, "undergraduatedegreestextcontainer")
temp = container.find_elements(By.TAG_NAME, "p")

majors = []
# add to majors list
for test in temp:
    test = test.find_element(By.TAG_NAME, "a")
    title = test.text
    # skip GIRs for now
    if title == "General Bachelor of Science Degree Requirements":
        continue
    try:
        link = test.get_attribute("href")
        link.click()
        driver.implicitly_wait(20)
    except:
        continue

print("majors length:", len(majors))

# loop through majors
for major in majors:
    print("major:", major)
    try:
        link = major.get_attribute("href")
        link.click()
        print("clicked")
        driver.implicitly_wait(10)
    except:
        continue
    
    # get major name and potential rows for courses
    name = driver.find_element(By.CLASS_NAME, "page-title")
    print("major:", name)
    potential = driver.find_elements(By.TAG_NAME, "tr") # all rows in table

    # only keep valid courses
    courses = []
    for course in potential:
        temp = course.find_element(By.TAG_NAME, "span")
        temp = temp.get_attribute("class")
        if "courselistcomment" in temp:
            continue
        else:
            temp = course.find_elements(By.TAG_NAME,"td")
            print("temp length: ", str(len(temp)))
            course_name = temp[1].text # second one has the name
            courses.append(course_name)
    
    major_to_courses[name] = courses
    print(name, courses)
    driver.back()

    for major in major_to_courses:
        for course in major_to_courses[major]:
            if course in course_to_majors:
                course_to_majors[course].append(major)
            else:
                course_to_majors[course] = major


    print(major for major in major_to_courses)

time.sleep(3)
