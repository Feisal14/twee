import csv
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver import Firefox


PATH= "D:\Downloads\ChromeDriver\geckodriver.exe"

driver = webdriver.Firefox() 

driver.get("https://twitter.com/login")
