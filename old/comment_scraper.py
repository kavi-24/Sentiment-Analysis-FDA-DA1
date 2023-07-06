import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
from check_int_conn import is_connected
from jamspell_checker import fix_fragment
from gingerit_checker import spell_checker


r'''
In environment variables:
Add "C:\Program Files\R\bin" to PATH
Set R_HOME to "C:\Program Files\R"

Imp paths:
C:\Program Files\RStudio
'''


def scrape_comments() -> list:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if is_connected():
        print("Connected")
        flag = 1
        link = input("Enter link: ")

        options = Options()
        options.headless = True

        def get_comments() -> list:
            data = []
            with Chrome(executable_path="chromedriver114.exe", options=options) as driver:
                try:
                    wait = WebDriverWait(
                        driver,
                        1000  # increase if low internet speed
                    )
                    # https://www.youtube.com/watch?v=cZFJyJzYugs
                    # https://www.youtube.com/watch?v=mO0OuR26IZM&pp=ygUMZXh0cmFjdGlvbiAy
                    driver.get(link)
                except:
                    # driver.get(
                    #     "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D"
                    # )
                    get_comments()

                # 10 x 3 = 30 seconds of scrolling
                for _ in range(10):
                    # print("Scrolling...")
                    wait.until(EC.visibility_of_element_located(
                        (By.TAG_NAME, "body"))).send_keys(Keys.END)
                    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(3)  # increase to delay scroll down speed

                for comment in wait.until(EC.presence_of_all_elements_located((By.ID, "content-text"))):
                    if (comment.text.strip() != ''):
                        try:
                            corrected = spell_checker(fix_fragment(comment.text))
                        except:
                            corrected = comment.text
                        data.append(corrected)
                    # data.append(comment.text)
                return data
        data = get_comments()
    else:
        print("Proceeding with default data due to low or no internet connection.")
        flag = 0
        data = []
        with open('default.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row[0])
    return data, flag
