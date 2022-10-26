import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InstaFollower:
    
    def __init__(self):
        self.chrome_driver_path = 'S:\Code_Projects\Chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.SIM_ACC = 'rap'
    
    def find_followers(self):
        self.driver.get('https://www.instagram.com')
        search = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_bL"]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div')

        search.click()
        time.sleep(.5)
        search.send_keys(f'{self.SIM_ACC}')
        search.send_keys(Keys.ENTER)
        follower = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_bL"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        follower.click()

    def follow(self):
        button_list = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_bL"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        buttons = button_list.find_elements(By.TAG_NAME,'button')
        for t in buttons:
            t.click()