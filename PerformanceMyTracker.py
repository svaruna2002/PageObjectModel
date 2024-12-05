from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()

#login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(5)

#navigating to Performance Page
driver.find_element(By.LINK_TEXT, "Performance").click()
time.sleep(5)

#navigating to my tracker page
driver.find_element(By.XPATH, "//a[normalize-space()='My Trackers']").click()
time.sleep(3)

#view
driver.find_element(By.CSS_SELECTOR, "button[name='view']").click()
time.sleep(3)

#add button
driver.find_element(By.XPATH, "//button[normalize-space()='Add Log']").click()
time.sleep(3)

#log
driver.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("Time Management")
time.sleep(3)

#negative
driver.find_element(By.XPATH, "//button[normalize-space()='Positive']").click()
time.sleep(3)

#positive
driver.find_element(By.XPATH, "//button[normalize-space()='Positive']").click()
time.sleep(4)

#comment
driver.find_element(By.XPATH, "//textarea[@placeholder='Type here']").send_keys("Good Job")
time.sleep(5)

#save
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(3)

#cancel
# driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
# time.sleep(3)