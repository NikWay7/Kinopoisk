from msilib.schema import Class
import time
from selenium.webdriver.common.by import By

import undetected_chromedriver.v2 as uc

class one : 

    driver = uc.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.kinopoisk.ru/special/birthday19/")    
    time.sleep(2)
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/button").click()

    time.sleep(1000)
    driver.quit()
