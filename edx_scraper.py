import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.edx.org/search?tab=course")

# store all data in dictionary mapping course name -> text
course_info = {}

# loop through all courses on website
course_per_page = 24
page = 1
total_pages = 42
# total_pages = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[4]/div/div/div[1]/nav/ul/li[6]/button")
# click on all courses in a page

# while page <= total_pages:
#     # click on current page
#     if page != 1:
#         page += 1
#         curr_page = driver.find_element(By.CLASS_NAME, "page-item active")
#         curr_page.click()
        # get all course on current page
    
driver.implicitly_wait(20)
courses = driver.find_elements(By.CLASS_NAME, "base-card-wrapper")
# For each course, get dropdown to choose What you'll learn section
driver.implicitly_wait(30)

for course in courses:
    driver.implicitly_wait(20)
    course.click()
    # Get course name
    # title = driver.find_element(By.CLASS_NAME, "col-md-7")
    # name = title.find_element(By.TAG_NAME, "h1").text
    # print(name)

    # Get What you'll learn section
    driver.implicitly_wait(30)
    section = driver.find_elements(By.CLASS_NAME, "preview-expand-component")

    index = None
    # Find index of What you'll learn
    for test in range(len(section)):
        if section[test].find_element(By.TAG_NAME, "h1").text == "What you'll learn":
            index = test
            break

    # index into correct section
    # section = driver.find_elements(By.CLASS_NAME, "preview-expand-body")[index]
    # Iterate through bullet points
    driver.implicitly_wait(10)
    bullets = section[index].find_elements(By.TAG_NAME, "p")
    if not bullets:
        bullets = section[index].find_elements(By.TAG_NAME, "li")

    # extract text from the section
    driver.implicitly_wait(10)
    print(bullets)
    for bullet in bullets:
        print(bullet.text)

    driver.implicitly_wait(10)
    driver.back()


    # for course in courses:
    #     #print("Course", course)
    #     course.click()
        
    #     button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[3]/div[1]/div[2]/div/a")
    #     # dropdown = Select(driver.find_element(By.CLASS_NAME, 'my-2 bg-white show dropdown')) 
    #     # dropdown.select_by_visible_text("What you'll learn")

    #     # go back to page with course lists
    #     # driver.back()

time.sleep(3)