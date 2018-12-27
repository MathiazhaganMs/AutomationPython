'''
Created on Dec 23, 2018

@author: Mathi
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class SignGoogle():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "C:\\Users\\Mathi\\Documents\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://automate.io/app")
        driver.find_element(By.XPATH,"//button[text()='Sign in with Google']").click()
        time.sleep(5)
        driver.find_element(By.ID,"identifierId").send_keys("msmathipy@gmail.com")
        driver.find_element(By.XPATH,"//span[text()='Next']").click()
        time.sleep(5)
        driver.find_element(By.NAME,"password").send_keys("Msdfan0207@")
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[text()='Next']").click()
        time.sleep(5)
        AccountIcon=driver.find_element(By.XPATH,"//img[@class='profile-image']")
        if AccountIcon is not None:
            print("Sign_in Successful")
        else:
            print("Sign_in Failed")
        driver.close()
        
        
ff = SignGoogle()
ff.test()