from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from decouple import config
from login_page import login_page_objects

def log_user(driver):
    user_text_edit =  driver.find_element(By.XPATH, login_page_objects.login) #username_text_edit to jest xpath | z _elem to elementy na ktorych dzialam
    user_text_edit.send_keys(config("USER"))
    password_text_edit =  driver.find_element(By.XPATH, login_page_objects.password) #password_text_edit
    password_text_edit.send_keys(config("USER_PASS"))
    submit_button = driver.find_element(By.XPATH, login_page_objects.save_button_xpath) #loginbutton
    submit_button.click()
    time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(config("HOST"))
    log_user(driver)