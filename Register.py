from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class Register():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "C:\\Users\\Mathi\\Documents\\chromedriver_win32\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://automate.io/app")
        driver.find_element(By.XPATH,"//a[text()='REGISTER']").click()
        driver.find_element(By.ID,"name").send_keys("Mathiazhagan")
        driver.find_element(By.ID,"email").send_keys("abc1233169@gmail.com")
        driver.find_element(By.ID,"password").send_keys("Mat@1236")
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[text()='REGISTER']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@class='btn btn-cta1 mw7']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@class='skip-link']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//i[@class='icon-close']").click()
        time.sleep(3)
        AccountIcon=driver.find_element(By.XPATH,"//img[@class='profile-image']")
        if AccountIcon is not None:
            print("Registration Successful")
        else:
            print("Registration Failed")
ff = Register()
ff.test()