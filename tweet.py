import pandas as pd
import os
import csv
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox


PATH= "D:\Downloads\ChromeDriver\geckodriver.exe"

driver = Firefox() 

driver.get("https://twitter.com/login")


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
search_input.send_keys("#covid19")
search_input.send_keys(Keys.ENTER)

# sleep(3)
# latest = driver.find_element(By.XPATH, "//span[contains(text(), 'Latest')]")
# latest.click()



userTags = []

tweets = []
replys = []
likes = []

last_position = driver.execute_script("return window.pageYOffset;")

# tweets = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

    
    
while True:
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    for article in articles:
        
        
        userTag = driver.find_element(By.XPATH, '//div[@data-testid="User-Name"]').text
        userTags.append(userTag)
        
        # time = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        # times.append(time)
        
        tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text
        tweets.append(tweet)
        
        reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        replys.append(reply)
        
        like = driver.find_element(By.XPATH, ".//div[@data-testid='like']")          
        likes.append(like)
                  
        
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")    
    uniq_tweets = list(set(tweets))
    if len(uniq_tweets) > 25:
        break

print(len(userTags),len(tweets)) 



df = pd.DataFrame(zip(userTags, tweets, replys, likes)
                  ,columns=['UserTags', 'Tweets', 'Time', 'Reply', 'Likes' ])

df.to_excel(r"D:\\PROJECTS\\Excel\\Tweets.xlsx", index=False)
df.head()

os.system('start "excel" "D:\\PROJECTS\\Excel\\Tweets.xlsx"' )

driver.quit()