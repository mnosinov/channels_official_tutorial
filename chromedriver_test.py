import os
import time
from selenium import webdriver
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
chromedriver_path = os.path.join(BASE_DIR, 'chromedriver/chromedriver')
print(chromedriver_path)
driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
