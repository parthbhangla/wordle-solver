# imports
import time
import random
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WordlePlayer:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options = self.options)
        self.word_list = self.load()

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
        time.sleep(1)

        # wordle inspect: there's three states - absent, present and correct so modify list on that basis
        # it also allows only 6 attemps, so could be a loop idea
        # random word from the file to start and over again to second guess

        # basic idea:
        # guess a word, start a loop (maybe on attempt basis), check states of the letters in the guess
        # on the basis on states of the letters, search and eliminate words from the original list
        # pick another random word and run the same loop over and over again until correct word = Found

        self.load() # loading the list

        word = random.choice(self.word_list) # random word from the list
        print(word) # check

        attempts = 0 # setting attempts to 0
        guess = False # variable for future check

        for attempts in range (0, 6):
            attempts = attempts + 1
            word = random.choice(self.word_list)
            letters = []
            for letter in word:
                letters.append(letter)
                button = self.driver.find_element(by = "class name", value = "")

if __name__ == "__main__":
    WordlePlayer().play()