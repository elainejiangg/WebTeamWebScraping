from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.edx.org/search?tab=course")
button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[4]/div/div/div[2]/div[1]/a")
button.click()

dropdown = Select(driver.find_element(By.ID, 'mobile-nav'))
# button.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div[4]/div/div[3]/div/div[2]")

