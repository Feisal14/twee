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
search_input.send_keys("#RiyadhSeason")
search_input.send_keys(Keys.ENTER)

sleep(3)
latest = driver.find_element(By.XPATH, "//span[contains(text(), 'Latest')]")
latest.click()


for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

tweets = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
for tweet in tweets:
    tweet_text = tweet.text
    print(tweet_text)
    
driver.quit()