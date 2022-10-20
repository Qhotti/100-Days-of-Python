import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

chrome_driver_path = 'S:\Code_Projects\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

EMAIL = os.environ.get('LINKEDIN_EMAIL')
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

linked_email = driver.find_element(By.ID,'username')
linked_email.send_keys(EMAIL)

linked_password = driver.find_element(By.ID,'password')
linked_password.send_keys(PASSWORD)

button = driver.find_element(By.TAG_NAME,'button')
button.click()


my_network = driver.find_element(By.XPATH,'//*[@id="global-nav"]/div/nav/ul/li[2]/a')
driver.implicitly_wait(4)
my_network.click()

driver.implicitly_wait(10)

follow_list = driver.find_element(By.XPATH,'//*[@id="main"]/ul')
f = driver.find_elements(By.CSS_SELECTOR, 'li ul li div section div div button')

for t in f:
    t.click()
    time.sleep(1)


