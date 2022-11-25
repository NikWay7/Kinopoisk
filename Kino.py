import time
from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc

#a = input() #выбрать мини-игру
#if a == 1: #2 мини-игра
class one : # создать потом 2 класс
        driver = uc.Chrome(executable_path="chromedriver.exe")
        driver.get("https://www.kinopoisk.ru/special/birthday19/")    
        time.sleep(3)
        element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/button").click() #регистрция
        time.sleep(5)
        element = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[2]/div/button[3]/span[2]').click() #QR
        time.sleep(30)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div/div/div[2]/div/div[2]/div[2]/div/button').click() #игра 2
        time.sleep(10)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/button').click() #начать
        time.sleep(5)
        for i in range (100,0,-1):
                for i in range (100,0,-1):
                        s = []
                        s2 = []   
                        element1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]") # last heal
                        c = len(s)
                        while element1.get_attribute('class') != "game__test-life-item game__test-life-item_dead":
                                text = driver.find_element(By.CLASS_NAME, 'game__test-question').text #вопрос
                                n = 0
                                while n < c:
                                        if text == s[n-1]: 
                                                driver.find_element(By.LINK_TEXT, s2[n]).click()
                                                n+=1                
                                else:
                                        #s.append(text)#'map' object has no attribute 'append'
                                        MyFile = open ('output.txt', 'a')
                                        s = map (lambda x: x + '\n', s)
                                        MyFile.writelines(text + '\n')
                                        MyFile.close()
                                        time.sleep(3)
                                        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/span').click()
                                        time.sleep(3)
                                        if driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[3]").get_attribute('class') == "game__test-life-item": #or  driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]").get_attribute('class') == "game__test-life-item":
                                                MyFile2 = open ('output2.txt', 'a')
                                                otvet = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/span').text
                                                s2 = map (lambda x: x + '\n', s2)
                                                MyFile2.writelines(otvet + '\n')
                                                MyFile2.close()
                                        elif driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]").get_attribute('class') == "game__test-life-item":
                                                MyFile2 = open ('output2.txt', 'a')
                                                otvet = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/span').text
                                                s2 = map (lambda x: x + '\n', s2)
                                                MyFile2.writelines(otvet + '\n')
                                                MyFile2.close()
                                        else:       
                                                MyFile2 = open ('output2.txt', 'a')
                                                s2 = map (lambda x: x + '\n', s2)
                                                time.sleep(4)
                                                otvet = driver.find_element(By.CLASS_NAME, 'modal-wrong-answer__title').text 
                                                time.sleep(3)
                                                MyFile2.writelines(((otvet[otvet.find("«") + 1:]).split('»')[0]) + '\n')
                                                MyFile2.close()
                                                time.sleep(3)
                                time.sleep(3)      
                                if element1.get_attribute('class') == "game__test-life-item game__test-life-item_dead":
                                        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div/div[3]/button[1]').click()
                        '''     else:
                                        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div/button').click()###
                                        '''
                time.sleep(2)
        driver.quit()