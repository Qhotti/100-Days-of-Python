from selenium import webdriver
from selenium.webdriver.common.by import By
from speedtest import InternetSpeedTwitterBot
import os




bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if bot.up < bot.PROMISED_UP and bot.down < bot.PROMISED_DOWN:
    bot.tweet_at_provider()
