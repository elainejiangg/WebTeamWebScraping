import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import json

driver = webdriver.Chrome()
course_info = []
course_num = 1

num_pages = 42
for num_pg in range(1, num_pages+1):
    print("________________________")
    print("PG #", num_pg)
    driver.get(f"https://www.edx.org/search?tab=course&page={num_pg}")

    time.sleep(3)


    courses = driver.find_elements(By.CLASS_NAME, "base-card-wrapper")
    num_courses_on_page = len(courses)


    # print("COURSES:", courses)
    print("NUM COURSE ON PG:", num_courses_on_page)
        
    for course_idx in range(num_courses_on_page):
        close_chat_Xpath = "/html/body/div[1]/div[1]/div/div[3]/div/div/div/button"

        try:
            close_chat_button = driver.find_element(By.XPATH, close_chat_Xpath)
            close_chat_button.click()
        except Exception as e:
            print(f'ERROR: {e}')
            print("NO CHAT")

        # print("____________")
        course_button = courses[course_idx]

        actions = ActionChains(driver)
        actions.move_to_element(course_button).perform()
        course_button.click()

        time.sleep(2)

        title_Xpath = "/html/body/div[1]/div[1]/div/main/div/div[1]/div/div[5]/div[1]/h1"
        title = driver.find_element(By.XPATH, title_Xpath).text
        time.sleep(1)

        # expand all using show more/all
        try:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            print("BUTTONS", buttons)
            show_more_buttons=[]
            for button in buttons:
                if button.text == "Show more":
                    show_more_buttons.append(button)
                if button.text == "show all":
                    show_more_buttons.append(button)
            # show_more_buttons = driver.find_elements(By.CLASS_NAME, show_more_classname)
            # print("SHOWMORE_BUTTONS: ", show_more_buttons)
            
            for button in show_more_buttons:
                actions.move_to_element(button).perform()
                button.click()
        except Exception as e:
            print(f'ERROR: {e}')
            print("NO SHOWMORE")

        
        try:
            descrip = driver.find_element(By.CLASS_NAME,"p")
            descrip = descrip.find_element(By.TAG_NAME, "p").text
        except Exception as e:
            descrip = ""
            print(f'ERROR: {e}')
        
        if descrip =="":
            try:
                descrip_Xpath = "/html/body/div[1]/div[1]/div/main/div/div[1]/div/div[5]/div[1]/div/p"
                descrip = driver.find_element(By.XPATH, descrip_Xpath).text
            except Exception as e:
                print(f'ERROR: {e}')

        # print("DESCRIP", descrip)

        try:
            course_duration_Xpath = "/html/body/div[1]/div[1]/div/main/div/div[2]/div/div[1]/div/div/div[1]/div/div[1]"
            course_duration = driver.find_element(By.XPATH, course_duration_Xpath).text
        except:
            course_duration = ""
        
        try:
            hours_per_week_Xpath = "/html/body/div[1]/div[1]/div/main/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]"
            hours_per_week = driver.find_element(By.XPATH, hours_per_week_Xpath).text
        except:
            hours_per_week = ""

        try:
            pacing_Xpath = "/html/body/div[1]/div[1]/div/main/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]"
            pacing = driver.find_element(By.XPATH, pacing_Xpath).text
        except:
            pacing = ""

        try:
            cost_Xpath = "/html/body/div[1]/div[1]/div/main/div/div[2]/div/div[1]/div/div/div[3]/div/div[1]"
            cost = driver.find_element(By.XPATH, cost_Xpath).text
        except:
            cost = ""

        at_a_glance = driver.find_element(By.CLASS_NAME, "at-a-glance") 
        li_glance = at_a_glance.find_elements(By.TAG_NAME,"li")
        # print("GLANCE", li_glance)
        # print("LEN GLA", len(li_glance))



        instition = ""
        subject = ""
        # descrip = ""
        level = ""
        prereq = ""
        language = ""
        video_transcripts = ""
        assoc_skills = ""
        assoc_programs = []

        for li in li_glance:
            try:
                header = li.find_element(By.TAG_NAME, "span").text
                if header == "Institution:":
                    try:
                        instition = li.find_element(By.TAG_NAME, "a").text
                        
                    except Exception as e:
                        instition = ""
                        print(f'ERROR: {e}')
                    if instition == "":
                        try:
                            instition = li.find_element(By.TAG_NAME, "p").text
                        except Exception as e:
                            instition = ""
                            print(f'ERROR: {e}')
                if header == "Subject:":
                    try:
                        subject = li.find_element(By.TAG_NAME, "a").text
                        
                    except Exception as e:
                        subject = ""
                        print(f'ERROR: {e}')
                    if subject == "":
                        try:
                            subject = li.find_element(By.TAG_NAME, "p").text
                        except Exception as e:
                            subject = ""
                            print(f'ERROR: {e}')
                if header == "Level:":
                    try:
                        level = li.find_element(By.TAG_NAME, "a").text
                        
                    except Exception as e:
                        level = ""
                        print(f'ERROR: {e}')
                    if level == "":
                        try:
                            level = li.text.split("Level: ")[1]
                        except Exception as e:
                            level = ""
                            print(f'ERROR: {e}')
                if header == "Prerequisites:":
                    try:
                        prereq = li.find_element(By.TAG_NAME, "a").text
                        
                    except Exception as e:
                        prereq = ""
                        print(f'ERROR: {e}')
                    if prereq == "":
                        try:
                            prereq = li.find_element(By.TAG_NAME, "p").text
                        except Exception as e:
                            prereq = ""
                            print(f'ERROR: {e}')
                    if prereq == "":
                        try:
                            prereq = li.find_element(By.TAG_NAME, "div").text
                        except Exception as e:
                            prereq = ""
                            print(f'ERROR: {e}')
                if header == "Language:":
                    
                    try:
                        language = li.text.split("Language: ")[1]
                        
                    except Exception as e:
                        language = ""
                        print(f'ERROR: {e}')
                    if language == "":
                        try:
                            langauge = li.text
                        except Exception as e:
                            language = ""
                            print(f'ERROR: {e}')
                if header == "Video Transcripts:":
                    try:
                        video_transcripts = li.text.split("Video Transcripts: ")[1]
                    except Exception as e:
                        video_transcripts = ""
                        print(f'ERROR: {e}')
                if header == "Video Transcript:":
                    try:
                        video_transcripts = li.text.split("Video Transcript: ")[1]
                    except Exception as e:
                        video_transcripts = ""
                        print(f'ERROR: {e}')

                if header == "Associated skills:":
                    try:
                        assoc_skills= li.find_elements(By.TAG_NAME, "span")[1].text
                    except Exception as e:
                        assoc_skills = ""
                        print(f'ERROR: {e}')
                    if assoc_skills == "":
                        try:
                            assoc_skills= li.find_element(By.TAG_NAME, "p").text
                        except Exception as e:
                            assoc_skills = ""
                            print(f'ERROR: {e}')
                if header == "Associated programs:":
                    try:
                        assoc_prog = li.find_element(By.TAG_NAME, "ul" )
                        assoc_progs = assoc_prog.find_elements(By.TAG_NAME, "li" )
                        for prog in assoc_progs:
                            prog_text = prog.find_element(By.TAG_NAME, "a").text
                            assoc_programs.append(prog_text)
                    except Exception as e:
                        assoc_programs= []
                        print(f'ERROR: {e}')

            except Exception as e:
                print(f'ERROR: {e}')

        # print("INSTITION:", instition)
        print("TITLE:", title)
        print("COURSE NUM: ", course_num)
        course_num+=1

        time.sleep(1)
        sections = driver.find_elements(By.CLASS_NAME, "preview-expand-component")

        # print("SECTION", sections)
        # print("LEN:", len(sections))

        about_section_idx = 0
        learn_section_idx = 0
        

        for sections_idx in range(len(sections)):
            section_ele = sections[sections_idx]

            try:
                header = section_ele.find_element(By.TAG_NAME, "h1").text
                if header == "What you'll learn":
                    learn_section_idx = sections_idx
                if header == "About this course":
                    about_section_idx = sections_idx
            except Exception as e:
                print(f'ERROR: {e}')

        # print("IDX:", sections_idx)

        learn_section = sections[learn_section_idx]
        learn_bullets = learn_section.find_elements(By.TAG_NAME, "li")

        about_section = sections[about_section_idx]
        about_bullets = about_section.find_elements(By.TAG_NAME, "p")

        if learn_bullets == []:
            learn_bullets = learn_section.find_elements(By.TAG_NAME, "p")

        about_all_bullets_info = []
        learn_all_bullets_info =[]
        


        show_more_classname = 'preview-expand-cta btn btn-link mt-2 pt-1 pt-sm-2 px-0 pb-0'


        time.sleep(1)

        for a_bullet in about_bullets:
            bullet_info = "default"
            try:
                bullet_info = a_bullet.text
            except Exception as e:
                bullet_info = ""
                print(f'ERROR: {e}')
            if bullet_info =="":
                try:
                    bullet_info = a_bullet.find_element(By.TAG_NAME, "p")
                except Exception as e:
                    bullet_info = ""
                    print(f'ERROR: {e}')
            about_all_bullets_info.append(bullet_info)
            # print(bullet_info)


        for l_bullet in learn_bullets:
            bullet_info = "default"
            try:
                bullet_info = l_bullet.text
            except Exception as e:
                bullet_info = ""
                print(f'ERROR: {e}')
            if bullet_info =="":
                try:
                    bullet_info = l_bullet.find_element(By.TAG_NAME, "p")
                except Exception as e:
                    bullet_info = ""
                    print(f'ERROR: {e}')
            learn_all_bullets_info.append(bullet_info)
            # print(bullet_info)
        
        
        dic = {}
        # [
        #     { title: , 
        #      instituion: ,
        #      date: ,
        #      descrip: ,
        #      stars: ,
        #      weeks: , 
        #      hours/week: ,
        #      pace: ,
        #     about: , 
        #     learn: ,
        #     syllabus: , 
        #     }
        # ]
        dic["title"] = title
        dic["instition"] = instition
        dic["subject"] = subject
        dic["descrip"] = descrip
        dic["level"] = level
        dic["prereq"] = prereq
        dic["langauge"] = language
        dic["video_transcripts"] = video_transcripts
        dic["assoc_skills"] = assoc_skills
        dic["assoc_programs"] = assoc_programs
        dic["course_duration"] = course_duration
        dic["hours_per_week"] = hours_per_week
        dic["pace"] = pacing
        dic["cost"] = cost
        # dic["li_len"] = len(li_glance)
        
        
        dic["about"] = about_all_bullets_info
        dic["learn"] = learn_all_bullets_info


        course_info.append(dic)
        with open('edx_9.json', 'w') as f:
            json.dump(course_info, f)
        
        driver.back()
        time.sleep(1)

