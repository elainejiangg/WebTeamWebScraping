import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://lexfridman.com/podcast/")

podcast_content = [] # list of dicts, each dict represents 
# id, title, guest, transcript, podcast number?

# first click on show all
buttons = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/div/div[2]")
button = buttons.find_elements(By.TAG_NAME, "button")[1] # second button
button.click()
driver.implicitly_wait(20)

# get all podcasts
grid = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/div/div[3]")
# grid = driver.find_element(By.CLASS_NAME, "grid grid-main")

all_podcasts = grid.find_elements(By.CLASS_NAME, "grid-item main-grid-item")
print(len(all_podcasts))
curr_podcast = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/div/div[3]/div[2]")

for podcast in all_podcasts:
    # click on podcast
    thumbnail = podcast.find_element(By.CLASS_NAME, "thumb-youtube")
    podcast_click = thumbnail.find_element(By.TAG_NAME, "a")
    podcast_click.click()
    driver.implicitly_wait(20)

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

    # podcast number
    # primary = driver.find_element(By.ID, "primary")
    # content = primary.find_element(By.ID, "content")
    # header = content.find_element(By.TAG_NAME, "header")
    # print(header.get_attribute("class"))
    # # get last item which is the episode number, take out # sign
    # print(header.find_element(By.CLASS_NAME, "entry-title").text)
    # l = (header.find_element(By.TAG_NAME, "h1").text).split()
    # print(l)
    # string = l[-1]
    # number = string[1:]
    # # number = (header.find_element(By.CLASS_NAME, "entry-title").text).split()[-1][1:]
    # pod_dict["podcast number"] = number
    # print("number:", number)

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

print("done")
time.sleep(3)