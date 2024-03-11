# Importing required libraries

# pip install selenium

from selenium import webdriver
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(8)

# clicking the new release hyperlink in the website
newreleases_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[3]")
newreleases_link.click()

# Waiting for the new release details page to load
time.sleep(2)

# clicking the hot new release hyperlink in the website
hotnewreleases_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/ul/li[2]/div/a")
hotnewreleases_link.click()

# Waiting for the hotnewreleases details page to load
time.sleep(3)

# clicking home hyperlink in the website
home_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[6]")
home_link.click()

# Waiting for the home details page to load
time.sleep(4)

# clicking the furniture hyperlink in the website

furniture_link = driver.find_element("xpath","//html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/a/img")
furniture_link.click()

# Waiting for the furniture details page to load
time.sleep(4)





# Closing the webdriver
driver.close()
