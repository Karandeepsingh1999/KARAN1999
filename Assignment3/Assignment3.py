from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the bestbuy homepage
driver.get("https://www.bestbuy.ca/en-ca")
time.sleep(3)

# Maximizing window
driver.maximize_window()

#Clicking the shop drop down
link = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/button/span")
link.click()
time.sleep(3)


#Clicking on Headphone,Speakers, Audio
Secondlink = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/div[2]/div/a[9]")
Secondlink.click()
time.sleep(3)

#Click on Home Audio and theatre
Thirdlink = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/div[2]/div/div[8]/div/a[1]")
Thirdlink.click()
time.sleep(5)

#Click on CD Player
Fourthlink = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/div[2]/div/div[8]/div/div[1]/div/a[6]")
Fourthlink.click()
time.sleep(10)



#Scrolling down the webpage
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)



search_bar = driver.find_element("id","email")
search_bar.send_keys("karan@gmail.com")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)


Fifthlink = driver.find_element("xpath","/html/body/div[1]/div/footer/div[1]/div/div[2]/div/div[3]/form/div/button/span")
Fifthlink.click()
time.sleep(10)


# Closing the webdriver
driver.close()