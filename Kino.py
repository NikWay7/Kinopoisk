from msilib.schema import Class
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
        time.sleep(7)
        element = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[2]/div/button[3]/span[2]').click() #QR
        time.sleep(25)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[1]/div/div/div/div[2]/div/div[2]/div[2]/div/button').click() #игра 2
        time.sleep(10)
        element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[1]/div/div/button').click() #начать
        time.sleep(5)
         
        s = []
        #s2 = []
        for i in range (2,0,-1):
           element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]")
           while element.get_attribute('class') != "game__test-life-item game__test-life-item_dead":
                with open('output.txt') as file: #получаем список исходя из файла с текстом(потом туда будут добавлятся элементы вследствие чего и список будет увеличиваться)
                    for line in file:
                        s.append(line)

                text = driver.find_element(By.CLASS_NAME, 'game__test-question').text
                for n in range (len(s),0,-1):
                    if text == s[n]:
                        if driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/span').text == 

                MyFile = open ('output.txt', 'w')
                #MyFile2 = open ('output2.txt', 'w')
                s = map (lambda x: x + '\n', s)
                #s2 = map (lambda x: x + '\n', s2)  
                MyFile.writelines(s)
                #MyFile2.writelines(s2) 
                MyFile.close ()
                #MyFile2.close ()
                if element.get_attribute('class') == "game__test-life-item game__test-life-item_dead":
                   element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div/div[3]/button[1]').click()
                else:
                    print(9)

        time.sleep(15)
        driver.quit()
#elif a == 2:
#class two:
'''    
#list.append(x)	Добавляет элемент в конец списка 
        #element = driver.find_element(By.CLASS_NAME, 'game__test-question').text
        #print(element)
        #element.get_attribute('class') возвращает указанный элемент (Элемент)
'''