from bs4 import BeautifulSoup
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from lxml import html

class Brain:
    
    def __init__(self):
        self.form = 'https://forms.gle/HYqBe4dn3YQxc5hy7'
        self.zillow = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.8','Accept-Encoding': 'gzip, deflate'}
        self.links = []
        self.prices = []
        self.addresses = []
        
    def get_info(self):
        response = requests.get(self.zillow, headers=self.headers)
        webpage = response.text
        tree = html.fromstring(response.content)
        soup = BeautifulSoup(webpage, 'lxml')
        
        link = [self.links.append(s.get('href')) for s in soup.find_all('a',class_ = 'property-card-link')]
        
        prices = [s.getText() for s in soup.find_all('span', {"data-test": "property-card-price"})]
        for e in prices:
            t=e.split('+',1)[0] + '+'
            self.prices.append(t)
        
        address = [self.addresses.append(s.getText()) for s in soup.find_all('address', {'data-test':'property-card-addr'})]
        
    def input_info(self):
        chrome_driver_path = 'S:\Code_Projects\Chromedriver\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        
        driver.get(self.form)
        total = len(self.links)
        count = 0

        while count != total:
            input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input.click()
            time.sleep(.5)
            input.send_keys(self.addresses[count])
            input.send_keys(Keys.TAB)
            time.sleep(.5)
            driver.switch_to.active_element.send_keys(self.prices[count])
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(.5)
            driver.switch_to.active_element.send_keys(self.links[count])
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(.5)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(.5)
            driver.switch_to.active_element.send_keys(Keys.TAB)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(.5)
            count+=1
    
                    
            