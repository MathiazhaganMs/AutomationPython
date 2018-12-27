from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class Login():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "C:\\Users\\Mathi\\Documents\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://automate.io/app")
        driver.find_element(By.XPATH,"//a[text()='LOGIN']").click()
        driver.find_element(By.ID,"email").send_keys("msmathipy@gmail.com")
        driver.find_element(By.ID,"password").send_keys("Msdfan0207@")
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[text()='LOGIN']").click()
        time.sleep(5)
        AccountIcon=driver.find_element(By.XPATH,"//img[@class='profile-image']")
        if AccountIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
    
        
        
ff = Login()
ff.test()
