

from constants import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class InternetSpeedBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        # cookies popup
        time.sleep(10)

        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(55)
        download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        if int(download) > PROMISED_DOWN and int(upload) > PROMISED_UP:
            exit()

    def tweet_at_provider(self):
        pass
