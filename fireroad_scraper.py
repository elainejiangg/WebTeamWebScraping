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

major_to_classes = []
date = 0
# date = time.mktime(datetime.timestamp(datetime.now()))
# id, title, date, metadata {}

# click on major on sidebar
major_count = 0
# menu = driver.find_element(By.ID, "majors")
# time.sleep(10)
# try:
#     menu = driver.find_element(By.ID, "majors")
#     time.sleep(10)
# except:
#     try:
#         menu = driver.find_element(By.CLASS_NAME, "sub-menu collapse in")
#         time.sleep(10)
#     except:
#         menu = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/ul[1]")
#         time.sleep(10)

# majors = menu.find_elements(By.TAG_NAME, "li")
# time.sleep(10)
# try:
#     majors = menu.find_elements(By.TAG_NAME, "li")
#     time.sleep(10)
# except:
#     print("majors not found")


# current major to look at
# major_titles = []
# for m in majors:
#     n = m.find_element(By.TAG_NAME, "strong")
#     major_titles.append(n.text)
# time.sleep(10)

menu = driver.find_element(By.ID, "majors")
time.sleep(10)
majors = menu.find_elements(By.TAG_NAME, "li")
time.sleep(10)
total_count = len(majors)

while major_count < total_count:
    # current major
    driver.get("https://fireroad-dev.mit.edu/requirements/edit/major1")
    time.sleep(20)
    try:
        menu = driver.find_element(By.ID, "majors")
    except:
        menu = driver.find_element(By.CLASS_NAME, "sub-menu collapse in")
    time.sleep(10)
    majors = menu.find_elements(By.TAG_NAME, "li")
    time.sleep(10)

    major = majors[major_count]
    print(major)
    time.sleep(10)
    major_count += 1

    # get major name
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


    # get all majors on side bar
    # try:
    #     ul = driver.find_element(By.CLASS_NAME, "sub-menu collapse in")
    #     time.sleep(10)
    # except:
    #     ul = driver.find_element(By.ID, "majors")
    #     time.sleep(10)

    # click into edit preview
    try:
        box = driver.find_element(By.CLASS_NAME, "content")
        time.sleep(10)
    except:
        try:
            box = driver.find_element(By.CLASS_NAME, "row edit-head")
            time.sleep(10)
        except:
            print("preview not found")
            continue

    try:
        preview = box.find_element(By.CLASS_NAME, "col s8 red-text text-darken-4")
        time.sleep(10)
    except:
        try:
            preview = box.find_element(By.ID, "preview-button")
            time.sleep(10)
        except:
            preview = box.find_element(By.TAG_NAME, "a")
            time.sleep(10)

    preview.click()
    time.sleep(10)

    # get courses
    # req_titles = []
    # try:
    #     req_titles = driver.find_elements(By.CLASS_NAME, "req-title")
    #     time.sleep(10)
    # except:
    #     print("req titles not found")

    metadata = {}

    course_nums = []
    course_titles = []
    try:
        classes_list = driver.find_elements(By.CLASS_NAME, "course-tile-outer")
        time.sleep(20)
        for c in classes_list:
            info = c.find_elements(By.TAG_NAME, "span")
            time.sleep(20)
            if len(info) == 1:
                course_nums.append(info[0].text)
                course_titles.append("")
            else:
                course_nums.append(info[0].text)
                course_titles.append(info[1].text)
    except:
        print("courses not found")
        continue

    # try:
    #     course_ids = driver.find_elements(By.CLASS_NAME, "course-id")
    #     time.sleep(10)
    #     course_nums = []

    #     for number in course_ids:
    #         if "units" in number.text:
    #             continue
    #         course_nums.append(number.text)

    #     course_names = driver.find_elements(By.CLASS_NAME, "course-title")
    #     time.sleep(10)
    #     course_titles = []
    #     for title in course_names:
    #         course_titles.append(title.text)
    # except:
    #     try:
    #         courses = driver.find_elements(By.CLASS_NAME, "course-tile-outer")
    #         time.sleep(10)
    #         temp_courses1 = []
    #         temp_courses2 = []

    #         for course in courses:
    #             ids = course.find_element(By.CLASS_NAME, "course-id").text
    #             if "units" in ids:
    #                 continue
    #             time.sleep(10)
    #             titles = course.find_element(By.CLASS_NAME, "course-title").text
    #             time.sleep(10)
    #             temp_courses1.append(ids)
    #             temp_courses2.append(titles)

    #         course_nums = temp_courses1
    #         course_titles = temp_courses2
    #     except: # don't include the __ units that don't have specific classes
    #         print("courses not found")
    #         continue

        # create the metadata for this major with course num, course title
    data = []
    print(len(course_nums), len(course_titles))
    for index in range(min(len(course_nums), len(course_titles))):
        data.append(course_nums[index] + " " + course_titles[index])
    metadata["classes"] = data

    # print(course_nums)
    # print(course_titles)
    # print(len(course_nums))
    # print(len(course_titles))

    id = uuid.uuid4()
    # title (major_name)
    title = name
    # date
    # date = time.mktime(datetime.now())
    # metadata? (classes that go into major)
    # metadata = {"classes": class_list}

    major_to_classes.append({"id": id, "title": title, "date": date, "metadata": metadata})


# map classes to major
classes_to_major = []
for dict in major_to_classes:
    data = dict["metadata"]
    major = dict["title"]
    # go through all classes in metadata
    for category in data:
        classes = data[category]
        for class_ in classes:
            if class_ in classes_to_major:
                classes_to_major[class_].append(major)
            else:
                classes_to_major[class_] = major
                
        
    
with open('job_data_11.json', 'w') as f:
    json.dump(major_to_classes, f)
    json.dump(classes_to_major, f)

driver.quit()
print("done")