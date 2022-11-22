from msilib.schema import Class
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import undetected_chromedriver.v2 as uc

class one : #открывает сайт втсавляет Название ищет
   

    driver = uc.Chrome(executable_path="C:\\Users\\Яна\\Desktop\учеба\\пиу\\проекты\\Kinopoisk\\chromedriver.exe")
    driver.get("https://www.kinopoisk.ru/special/birthday19/")
    time.sleep(15)
    element = driver.find_elements(executable_path="/html/body/div[1]/div/section[1]/div/div/div/div[3]/div/div[2]/div[2]/div/button").click #кнопка
#driver = webdriver.Chrome(executable_path="C:\\Users\\Яна\\Desktop\учеба\\пиу\\проекты\\Kinopoisk\\chromedriver.exe")

time.sleep(1000)
#driver.quit()