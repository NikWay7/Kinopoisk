from msilib.schema import Class
import time
from selenium.webdriver.common.by import By

import undetected_chromedriver.v2 as uc

class one : 

    driver = uc.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.kinopoisk.ru/special/birthday19/")    
    time.sleep(2)
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/button").click()
    time.sleep(2)
    element = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[2]/div/button[3]/span[2]').click()
    time.sleep(3)
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div/div/div[2]/div/div[2]/div[2]/div/button').click()
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/button').click()
    time.sleep(100)

    time.sleep(100)

    time.sleep(15)
    driver.quit()

#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/span 1
#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/span 2
#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[3]/div/span 3
#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[4]/div/span 4