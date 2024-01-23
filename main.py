# imports
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WordlePlayer:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options = self.options)
        self.word_l = self.load()

    def load(self):
        word_list = []
        f = open("answers.txt", "r")
        for line in f:
            line.strip()
            word_list.append(line)
        return word_list
    
    def play(self):
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        try:
            button = self.driver.find_element(by = "class name", value = "Welcome-module_button__ZG0Zh")
            button.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        try:
            button = self.driver.find_element(by = "class name", value = "Modal-module_closeIcon__TcEKb")
            button.click()
        except Exception as e:
            print(e)
        time.sleep(2)

if __name__ == "__main__":
    WordlePlayer().play()