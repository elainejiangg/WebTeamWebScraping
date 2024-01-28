import json
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.edx.org/search?tab=course")

# store all data in list of dictionaries
courses_info = []

# loop through all pages
page_num = 1
total_pages = 42

while page_num < total_pages:
    time.sleep(10)
    courses = driver.find_elements(By.CLASS_NAME, "base-card-wrapper")
    time.sleep(10)
    for course in courses:
        info = {} # id, title, description
        try:
            course.click()
            print("clicked")
        except Exception as e:
            print(f'ERROR: {e}')
            continue
        time.sleep(10)

        # uuid
        info["id"] = uuid.uuid4()

        # course title
        try:
            name = driver.find_element(By.CLASS_NAME, "col-md-7 pr-4")
            print("found first name")
        except:
            try:
                name = driver.find_element(By.CLASS_NAME, "col-md-7")
                print("found second name")
            except:
                continue

        name = name.find_element(By.TAG_NAME, "h1").text
        time.sleep(10)
        info["course title"] = name
        print(name)

        # what you'll learn section
        try:
            section = driver.find_element(By.CLASS_NAME, "preview-expand-body m-0")
            print("first what you'll learn")
        except:
            section = driver.find_element(By.CLASS_NAME, "preview-expand-body")
            print("second what you'll learn")
        driver.implicitly_wait(10)

        try:
            ul = section.find_element(By.TAG_NAME, "ul")
            driver.implicitly_wait(10)
            print("found ul")
        except:
            ul = section
        bullets = []
        try:
            bullets = ul.find_elements(By.TAG_NAME, "li")
            driver.implicitly_wait(10)
            print("found li")
        except:
            continue

        try:
            p_bullets = []
            for bullet in bullets:
                p_bullets.append(bullet.find_element(By.TAG_NAME, "p"))
                time.sleep(10)
            print("found p")
            bullets = p_bullets
        except:
            print("no p tag")

        print(len(bullets))

        if not bullets:
            continue

        for bullet in bullets:
            if "description" in info:
                info["description"].append(bullet.text)
            else:
                info["description"] = [bullet.text]
            driver.implicitly_wait(10)

        print(name, ": ", info["description"])
            
        driver.back()
        print("back to main page")


    driver.implicitly_wait(20)
    try:
        store_page = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div/div/div[1]/nav/ul")
        driver.implicitly_wait(20)
    except:
        try:
            store_page = driver.find_element(By.CLASS_NAME, "pagination")
            driver.implicitly_wait(20)
        except:
            continue
            

    try:
        all_pages = store_page.find_elements(By.TAG_NAME, "li")
        driver.implicitly_wait(20)
    except:
        all_pages = store_page.find_elements(By.CLASS_NAME, "page-item")
        driver.implicitly_wait(20)

#     # for p in all_pages:
#     #     if p.get_attribute("aria-label") == "Page" + str(page_num):
#     #         driver.implicitly_wait(20)
#     #         p.click()
#     #         break

    try:
        next_button = all_pages[len(all_pages)-1].find_element(By.TAG_NAME, "button")
        driver.implicitly_wait(20)
    except:
        next_button = all_pages[len(all_pages)-1].find_element(By.CLASS_NAME, "btn-icon btn-icon-primary btn-icon-md next page-link")
        driver.implicitly_wait(20)
    next_button.click()
    print("next page")
    driver.implicitly_wait(30)
    page_num += 1


# while page_num < total_pages:
#     print("page:", page_num)
#     driver.implicitly_wait(10)
#     courses = driver.find_elements(By.CLASS_NAME, "base-card-wrapper")

#     # loop through all courses on page
#     for course in courses:
#         driver.implicitly_wait(10)
#         try:
#             course.click()
#         except:
#             continue
#         driver.implicitly_wait(10)

#         # Get course name
#         try:
#             name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[1]/div/div[5]/div[1]/h1").text
#             driver.implicitly_wait(10)
#         except:
#             continue
#         # try:
#         #     name = driver.find_element(By.TAG_NAME, "h1").text
#         #     driver.implicitly_wait(10)
#         # except:
#         #     continue
#         print("Course:", name)

#         # Get What you'll learn section
#         # section = driver.find_elements(By.CLASS_NAME, "preview-expand-component")
#         ul = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[4]/div/div[3]/div/div[2]/div/ul")

#         index = None
#         # Find index of What you'll learn
#         # for test in range(len(section)):
#         #     try: 
#         #         compare = section[test].find_element(By.TAG_NAME, "h1").text
#         #         driver.implicitly_wait(10)
#         #     except:
#         #         continue
#         #     if compare == "What you'll learn":
#         #         index = test
#         #         break

#         # index into correct section
#         # section = driver.find_elements(By.CLASS_NAME, "preview-expand-body")[index]
#         # Iterate through bullet points
#         # if index is None:
#         #     print("course skipped")
#         #     continue

#         bullets = []
#         bullets = ul.find_elements(By.TAG_NAME, "li")
#         # try:
#         #     bullets = section[index].find_elements(By.TAG_NAME, "p")
#         #     driver.implicitly_wait(10)
#         # except:
#         #     print("Not in p")
#         #     bullets = section[index].find_elements(By.TAG_NAME, "li")
#         # if not bullets:
#         #     bullets = section[index].find_elements(By.TAG_NAME, "li")

#         # extract text from the section
#         driver.implicitly_wait(10)
#         # print(bullets)
#         for bullet in bullets:
#             course_info[name] = bullet.text
#             print(name, bullet.text)
#             driver.implicitly_wait(10)

#         driver.back()
#         print("Back to main page")

#     # logic for finding and clicking on the next page
#     driver.implicitly_wait(20)
#     try:
#         store_page = driver.find_element(By.CLASS_NAME, "pagination")
#         driver.implicitly_wait(20)
#     except:
#         page_num += 1
#         print("page not found")
#         continue

#     driver.implicitly_wait(20)
#     try:
#         all_pages = store_page.find_elements(By.CLASS_NAME, "page-item")
#         driver.implicitly_wait(20)
#     except:
#         page_num += 1
#         print("page not found")
#         continue

#     # for p in all_pages:
#     #     if p.get_attribute("aria-label") == "Page" + str(page_num):
#     #         driver.implicitly_wait(20)
#     #         p.click()
#     #         break

#     next_button = all_pages[len(all_pages)-1].find_element(By.TAG_NAME, "button")
#     next_button.click()
#     driver.implicitly_wait(20)
#     page_num += 1


with open('edx_courses.json', 'w') as f:
    json.dump(courses_info, f)

driver.quit()