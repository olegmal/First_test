import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sign_in():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    EMAIL = "//input[@id='Email']"
    PASSWORD = '#Password'
    LOG_IN = 'button[type="submit"]'

    email = driver.find_element(By.XPATH, EMAIL)
    email.send_keys('admin@yourstore.com')
    password = driver.find_element(By.CSS_SELECTOR, PASSWORD)
    password.send_keys('admin')
    submit = driver.find_element(By.CSS_SELECTOR, LOG_IN)
    submit.click()
    time.sleep(3)
    driver.quit()
