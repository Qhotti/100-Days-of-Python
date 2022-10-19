from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'S:\Code_Projects\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a') #finds article count

# content_portals = driver.find_element(By.LINK_TEXT,'Content portals') #finds hyperlink
# content_portals.click()

# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Lord of the Rings')         #search,type and enter
# search.send_keys(Keys.ENTER)

driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.CLASS_NAME, 'top')
first_name.send_keys('Frodo')

last_name = driver.find_element(By.CLASS_NAME, 'middle')
last_name.send_keys('Baggins')

email_name = driver.find_element(By.CLASS_NAME, 'bottom')
email_name.send_keys('lotr@gmail.com')
email_name.send_keys(Keys.ENTER)


# driver.quit()