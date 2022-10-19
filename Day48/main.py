from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'S:\Code_Projects\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get('https://www.amazon.com/All-new-Kindle-Paperwhite-adjustable-Ad-Supported/dp/B08KTZ8249/ref=sr_1_1?crid=4ZS9MXX13CY6&keywords=kindle&qid=1665787266&qu=eyJxc2MiOiI0LjQ4IiwicXNhIjoiNC4xMiIsInFzcCI6IjMuNzkifQ%3D%3D&s=amazon-devices&sprefix=kind%2Camazon-devices%2C216&sr=1-1')

#price = driver.find_element(By.CLASS_NAME,'a-price-whole')
                            #By.ID
                            #By.CSS_SELECTOR
                            #By.TAG_NAME



#print(price.text)

#driver.quit() #closes whole browser
#driver.close() #closes single tab



#Challenge 1: scrape website

# driver.get('https://www.python.org/')

# table = driver.find_element(By.CSS_SELECTOR,'.event-widget .shrubbery .menu')

# time = table.find_elements(By.CSS_SELECTOR, 'li time')
# event = table.find_elements(By.CSS_SELECTOR, 'li a')


# dict ={}
# count=0
# for (t,e) in zip(time, event):
#     dict[count] = {}
#     dict[count]['time']=t.text
#     dict[count]['event']=e.text
#     count+=1


# print(dict)










driver.quit()