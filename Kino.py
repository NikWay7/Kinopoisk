from msilib.schema import Class
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc

a = input()
if a == 1:
    class one : 
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
        time.sleep(10)

        for i in range (10,0,-1):
            1
        time.sleep(100)

        time.sleep(15)




        driver.quit()

else : #print("No")
    s = ["Самара", "Сочи", "Мурманск", "Анапа"]
    s2 = ["1", "2", "3", "4"]

    MyFile = open ('output.txt', 'w')
    MyFile2 = open ('output2.txt', 'w')
    s = map (lambda x: x + '\n', s)
    s2 = map (lambda x: x + '\n', s2)  
    MyFile.writelines(s)
    MyFile2.writelines(s2) 
    MyFile.close ()
    MyFile.close ()
    print (*s)

#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/span 1
#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/span 2
#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[3]/div/span 3
#/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[4]/div/span 4

#list.append(x)	Добавляет элемент в конец списка