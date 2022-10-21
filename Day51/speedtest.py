import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.chrome_driver_path = 'S:\Code_Projects\Chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.TWITTER_USER = os.environ.get('T_user')
        self.TWITTER_PASSWORD = os.environ.get('T_PASSWORD')
        self.PROMISED_DOWN = 1000
        self.PROMISED_UP = 50
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(5)
        go = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(60)
        d = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        u = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = d.text
        self.up = u.text


    
    def tweet_at_provider(self):
        self.driver.get('https://www.twitter.com/')
        time.sleep(2)
        sign_in = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()
        time.sleep(2)
        login = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login.send_keys(self.TWITTER_USER)
        time.sleep(3)
        login.send_keys(Keys.ENTER)
        time.sleep(2)
        password=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.TWITTER_PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(20)
        
        enter = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        enter.click()
        time.sleep(1)
        enter.send_keys(f'Hey @MediaComUS why am I getting {self.down}mbps down and {self.up}mbps up if I pay for {self.PROMISED_DOWN}down and {self.PROMISED_UP}up.')
        enter.send_keys(Keys.ENTER)
        
        