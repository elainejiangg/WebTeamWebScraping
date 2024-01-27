import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()
driver.get("https://careers.peopleclick.com/careerscp/client_mit/external/results/searchResult.html")

driver.implicitly_wait(10)

drop_down_Xpath ="/html/body/div/div/div/div[1]/div/div[2]/form/div[2]/div[6]/div/div/div/button"
drop_down_button = driver.find_element(By.XPATH, drop_down_Xpath)
drop_down_button.click()
fifty_Xpath = "/html/body/div/div/div/div[1]/div/div[2]/form/div[2]/div[6]/div/div/div/ul/li[4]/a"
fifty_button = driver.find_element(By.XPATH, fifty_Xpath)
fifty_button.click()


button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/form/div[2]/div[6]/div/button[2]")
button.click()
driver.implicitly_wait(10)

job_dic = {}

job_idx = 0
num_jobs_on_pg = 50
num_total_jobs_Xpath = "/html/body/div/div/div/div[1]/div/div/div[4]/form[1]/div/div[1]/span[1]"
num_total_jobs =  int(driver.find_element(By.XPATH, num_total_jobs_Xpath).text)
pg_clicks = int(num_total_jobs/num_jobs_on_pg)
print("NUM CLICKS:", pg_clicks)


pg_num = 1
for pg in range(0, pg_clicks+1):
    print("________________")
    print("pg#:", pg_num)
    time.sleep(1)
    # wait = WebDriverWait(driver, 10)
    # jobs_on_page = []
    jobs_on_page = driver.find_elements(By.CLASS_NAME, "pf-srp-singlehit")
    actual_num_jobs_on_page = len(jobs_on_page)
    print("# JOBS ON PG:", actual_num_jobs_on_page)

    for job in range(1, actual_num_jobs_on_page+1):
        driver.implicitly_wait(10)
        jobXpath = f"/html/body/div/div/div/div[1]/div/div/div[4]/form[2]/div/div[1]/ul/li[{job}]/div[1]/div[1]/div/label/a"
        job_info = {}

        try:
            job = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, jobXpath)))
            job.click()

            job_title_Xpath="/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[1]/div/span"
            job_number_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[1]/ul/li[1]/span[2]"
            functional_Area_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[1]/ul/li[2]/span[2]"
            department_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[1]/ul/li[3]/span[2]"
            school_Area_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[1]/ul/li[4]/span[2]"
            employment_Type_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[2]/ul/li[1]/span[2]"
            # /html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[2]/ul/li[1]/span[2]            
            employment_Cat_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[2]/ul/li[2]/span[2]"
            visa_Spon_Avail_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div/div[2]/ul/li[3]/span[2]"
            job_descrip_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[1]/p[2]"         
            job_req_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[2]/p[2]"
            
            # /html/body/div/div/div/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[2]/p[2]
            # /html/body/div/div/div/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[2]/p[2]
            job_title = driver.find_element(By.XPATH, job_title_Xpath).text
            job_number = driver.find_element(By.XPATH, job_number_Xpath).text
            functional_Area = driver.find_element(By.XPATH, functional_Area_Xpath).text
            department = driver.find_element(By.XPATH, department_Xpath).text
            school_Area = driver.find_element(By.XPATH, school_Area_Xpath).text
            employment_Type = driver.find_element(By.XPATH, employment_Type_Xpath).text
            employment_Cat = driver.find_element(By.XPATH, employment_Cat_Xpath).text
            visa_Spon_Avail = driver.find_element(By.XPATH, visa_Spon_Avail_Xpath).text
            
            try:
                job_descrip = driver.find_element(By.XPATH, job_descrip_Xpath).text
            except Exception as e:
                job_descrip = ""
                print(f'ERROR: {e}')

            if job_descrip=="":
                try:
                    job_descrip_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[1]/div/p[2]"
                    job_descrip = driver.find_element(By.XPATH, job_descrip_Xpath).text
                except Exception as e:
                    job_descrip = ""
                    print(f'ERROR: {e}')

            try:
                job_req = driver.find_element(By.XPATH, job_req_Xpath).text
                req = job_req.split("PREFERRED:", 1)[0].strip()
                req = req.split("REQUIRED:", 1)[1].strip()
                
            except Exception as e:
                req = ""
                print(f'ERROR: {e}')
            if req =="":
                try:
                   job_req_Xpath = "/html/body/div/div/div/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[2]/p[1]"
                   job_req = driver.find_element(By.XPATH, job_req_Xpath).text
                   req = job_req.split("PREFERRED:", 1)[0].strip()
                   req = req.split("REQUIRED:", 1)[1].strip()
                except Exception as e:
                    req = ""
                    print(f'ERROR: {e}')
            try:
                pre_num_date = job_req.split("PREFERRED:")[1]
                pre = pre_num_date.split("Job #", 1)[0].strip()
            except Exception as e:
                pre = ""
                print(f'ERROR: {e}')
            try:
                date = job_req.split("\n")[-1].strip()
                print(req)
                print("___________")
                print(pre)
                print("___________")
                print(date)
            except Exception as e:
                date = ""
                print(f'ERROR: {e}')
                
                
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("NUM:", job_idx)
            print(job_title)
            # print(job_number)
            # print(functional_Area)
            # print(department)
            # print(school_Area)
            # print(employment_Type)
            # print(employment_Cat)
            # print(visa_Spon_Avail)
            print("___________")
            print("DESCRIP", job_descrip)
            print("___________")
            print("REQ", job_req)
            print("___________")
            

            

            job_info["job_title"] = job_title
            job_info["job_number"] = job_number
            job_info["functional_Area"] = functional_Area
            job_info["department"] = department
            job_info["school_Area"] = school_Area
            job_info["employment_Type"] = employment_Type
            job_info["employment_Cat"] = employment_Cat
            job_info["visa_Spon_Avail"] = visa_Spon_Avail
            job_info["job_descrip"] = job_descrip
            job_info["job_req"] = req
            job_info["job_pre"] = pre
            job_info["date"] = date
            job_dic[job_idx] = job_info

            
            job_idx+=1
            back_button_Xpath = "/html/body/div/div/div/div[1]/div/div/div[1]/div/span/span/a"
            back_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, back_button_Xpath)))

            back_button.click()
        except Exception as e:
            print(f'An error occurred: {e}')
        
    time.sleep(1)
    next_pg_Xpath = "/html/body/div/div/div/div[1]/div/div/div[4]/form[1]/div/div[3]/ul/li[9]/a"

    if (pg_num%5==1 and pg_num >1):
        next_pg_Xpath = "/html/body/div/div/div/div[1]/div/div/div[4]/form[1]/div/div[3]/ul/li[8]/a"
        print("changed xpath")
    if (pg_num==(pg_clicks-1)):
        next_pg_Xpath = "/html/body/div/div/div/div[1]/div/div/div[4]/form[1]/div/div[3]/ul/li[8]/a"
        print("changed paths")
    next_pg_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, next_pg_Xpath)))
    
    next_pg_button.click()
    driver.implicitly_wait(10)
    print('CLICKED NEXT PG')
    pg_num+=1


        
with open('job_data_11.json', 'w') as f:
    json.dump(job_dic, f)

driver.quit()