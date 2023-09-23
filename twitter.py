import pandas as pd
import os
import csv
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox

driver = webdriver.Firefox() 

chrome_test = 'C:\\Users\\GLSK\\Downloads\\chrome-win64 (1)\\chrome-win64\\chrome.exe'

# options = webdriver.ChromeOptions()
# options.binary_location = chrome_test

# # PATH= "D:\Downloads\ChromeDriver\chromedriver.exe"
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://twitter.com/login")

driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

sleep(3)
username = driver.find_element(By.XPATH, "//input[@name= 'text']")
username.send_keys('tweetssike')
next_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]" )
next_btn.click()


sleep(4)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys('Ta12345678')
login = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]" )
login.click()


sleep(3)
search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search query"]')
search_input.send_keys("(#RiyadhSeason) until:2023-09-01 since:2020-09-01")
search_input.send_keys(Keys.ENTER)



cards = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
card = cards[0]

# user name
card.find_element(By.XPATH,'.//span').text
    
# handle
card.find_element(By.XPATH, '//span[contains(text(), "@")]').text

# date and time
card.find_element(By.XPATH, './/time').get_attribute('datetime')


comment = card.find_element(By.XPATH, './/div[2]/div[2]/div[1]').text
responding = card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text



# reply

card.find_element(By.XPATH, './/div[@data-testid="reply"]').text

# retweet

card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text

# likes 

card.find_element(By.XPATH, './/div[@data-testid="like"]').text

def get_tweet_data(card):
    
    """Extract data from tweet card"""
    
    username = card.find_element(By.XPATH,'.//span').text
    handle = card.find_element(By.XPATH, '//span[contains(text(), "@")]')
          
    try:
        postdate = card.find_element(By.XPATH, './/time').get_attribute('datetime')
    except NoSuchElementException:
        return
        
    comment = card.find_element(By.XPATH, './/div[2]/div[2]/div[1]').text
    responding = card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text
    text = comment + responding
    reply = card.find_element(By.XPATH, './/div[@data-testid="reply"]').text
    like = card.find_element(By.XPATH, './/div[@data-testid="like"]')
    retweet = card.find_element(By.XPATH, './/div[@data-testid="retweet"]')
    tweet = (username, handle, postdate, text, reply, like, retweet)
     
    return tweet

data = []
tweet_ids = set()
last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True

while scrolling: 
    page_card = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    for card in page_card[-15:]: 
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(str(tweet))                                                                                                                                                                                                                                   
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
            data.append(tweet)
        
        
    scroll_attempt = 0   
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        curr_position = driver.execute_script("return window.pageYOffset;")
        if last_position == curr_position:
            scroll_attempt += 1
            
            if scroll_attempt >= 3:
                scrolling = False
                break
            else:
                sleep(2)
        else:
            last_position = curr_position
            break


print(len(data))
df = pd.DataFrame(data, columns=['User', 'Handle', 'Timestamp', 'Text', 'Comments', 'Likes', 'Retweets'])

df.to_excel(r"D:\\PROJECTS\\Excel\\Tweets.xlsx", index=False)

os.system('start "excel" "D:\\PROJECTS\\Excel\\Tweets.xlsx"' )

driver.quit()