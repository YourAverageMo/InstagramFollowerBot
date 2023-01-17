import os
import time

from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# remember # is used for id and . is used for class

SIMILAR_ACCT = "chefsteps"  #dont really need this since u can access the same info using the below URL
LOGIN_URL = "https://www.instagram.com/accounts/login/"
ACCT_URL = "https://www.instagram.com/chefsteps/followers/"
CHROME_DRIVER_PATH = "/Users/momo/Development/chromedriver"


class InstaFollower():
    """responsible for all instagram data accessing"""

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            options=options,
            service=Service(executable_path=CHROME_DRIVER_PATH))

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(1)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)

        not_now = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button"
        )
        not_now.click()
        time.sleep(2)

        not_now2 = self.driver.find_element(By.CSS_SELECTOR, "._a9_1")
        not_now2.click()

    def follow(self):
        self.driver.get(ACCT_URL)
        time.sleep(2)

        followers_list_window = self.driver.find_element(
            By.CSS_SELECTOR, "._aano")

        while 1 > 0:
            followers_list = followers_list_window.find_elements(
                By.CSS_SELECTOR, "div div div")
            for item in followers_list:
                button = item.find_element(By.CSS_SELECTOR, "button")
                if button.text == "follow":
                    button.click()
                    time.sleep(2)

            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                followers_list_window)
            time.sleep(1)