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
        self.word_list = []

    def load(self):
        f = open("wordle-solver/accepted_words.txt", "r")
        for line in f:
            self.word_list.append(line.strip())
        return self.word_list

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

        self.load()

        guess = random.choice(self.word_list)

        attempts = 0
        found = False

        for attempts in range(6):
            attempts = attempts + 1
            if len(self.word_list) == 0:
                print("Word wasn't in the 'answers.txt' file")

            guess = random.choice(self.word_list)

            for letter in guess:
                keyboard.write(letter)
                time.sleep(0.2)

            time.sleep(0.2)

            keyboard.press_and_release("enter")

            time.sleep(2)

            row = ('div[class*="Board"] div[class*="Row-module"]:nth-of-type(%s) ' % attempts)

            tile = row + 'div:nth-child(%s) div[class*="module_tile__"]'

            try:
                element_present = EC.presence_of_element_located((By.CSS_SELECTOR, tile % "5" + '[data-state$="t"]'))
                WebDriverWait(self.driver, 10).until(element_present)
            except TimeoutError:
                print(f"Timed out waiting for element with locator: {tile % '5'} [data-state$='t']")

            feedback = []

            for i in range(1, 6):
                letter_eval = self.driver.find_element(By.CSS_SELECTOR, tile % str(i)).get_attribute("data-state")
                feedback.append(letter_eval)

            if feedback.count("correct") == 5:
                found = True
                break
            
            self.word_list.remove(guess)
            self.modify(guess, feedback)

        if found:
            print('\nWord: %s\nAttempts: %s' % (guess.upper(), attempts))
        else:
            print("Unable to guess and solve in 6 turns.")

        time.sleep(5)

    def modify(self, guess, feedback):
        filtered_words = set()

        for word in self.word_list:
            valid_word = True
        
            for i in range(len(guess)):
                if feedback[i] == "correct" and guess[i] != word[i]:
                    valid_word = False
                    break

                if feedback[i] == "present" and guess[i] == word[i]:
                    valid_word = False
                    break

                if feedback[i] == "absent" and guess[i] in word:
                    valid_word = False
                    break

            if valid_word:
                filtered_words.add(word)
        
        self.word_list = list(filtered_words)

if __name__ == "__main__":
    WordlePlayer().play()