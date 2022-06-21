from constants import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class InternetSpeedBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass

