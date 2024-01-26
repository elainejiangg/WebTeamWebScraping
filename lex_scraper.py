import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://lexfridman.com/podcast/")

podcast_content = [] # list of dicts, each dict represents 
# id, title, date, guest, duration of episode, transcript

# first click on show all
buttons = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/div/div[2]")
button = buttons.find_elements(By.TAG_NAME, "button")[1] # second button
button.click()
driver.implicitly_wait(20)

grid = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/div/div[3]")
curr_podcast = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/div/div[3]/div[2]")

# dictionary of each podcast
pod_dict = {}

# generate id
pod_dict["id"] = uuid.uuid4()

# video title
title = curr_podcast.find_element(By.CLASS_NAME, "vid-title").find_element(By.TAG_NAME, "a").text
print(title)
pod_dict["title"] = title

# guest name
guest = curr_podcast.find_element(By.CLASS_NAME, "vid-person").text
print(guest)
pod_dict["guest"] = guest

# transcript
materials = curr_podcast.find_element(By.CLASS_NAME, "vid-materials")
transcript_link = materials.find_elements(By.TAG_NAME, "a")[2] # the third one is transcript
transcript_link.click()
driver.implicitly_wait(20)
script = driver.find_elements(By.CLASS_NAME, "ts-segment")

# list of text for transcript, broken by sections
transcript = []
for section in script:
    text = section.find_element(By.CLASS_NAME, "ts-text").text
    transcript.append(text)
    
pod_dict["transcript"] = transcript
podcast_content.append(pod_dict)
print(podcast_content)

# podcasts = grid.find_elements(By.CLASS_NAME, "grid-item main-grid-item")

# print(len(podcasts))