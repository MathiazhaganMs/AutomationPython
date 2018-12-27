'''
Created on Dec 23, 2018

@author: Mathi
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class ForgetPassword():
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
        time.sleep(5)
        driver.find_element(By.LINK_TEXT,"Forgot Password?").click()
        driver.find_element(By.ID,"email").send_keys("msmathipy@gmail.com")
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[text()='Send Email']").click()
        time.sleep(5)
        checkMail=driver.find_element(By.XPATH,"//span[text()='Password reset email sent. Please read instructions in the email to proceed futher.']")
        if checkMail is not None:
            print("Check your email")
        else:
            print("Mail is wrong")
        driver.close()
        
ff = ForgetPassword()
ff.test()
        
                                                    