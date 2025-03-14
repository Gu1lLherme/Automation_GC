from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
login = "professorideal14@outlook.com"
senha = "abc@123456"

driver = webdriver.Chrome()
driver.get("https://lite.estuda.com/usuarios_login")

driver.maximize_window()

assert "Login" in driver.title

    
login_intput = driver.find_element(by= By.NAME,value="siu_email")
login_intput.send_keys(login)

pass_input = driver.find_element(by=By.ID, value="pass-input")
pass_input.send_keys(senha)

# Button to send form

driver.find_element(by=By.XPATH, value='//*[@id="frm_login"]/div/div[1]/button').click()

time.sleep(50)



