import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

@pytest.mark.usefixtures("chrome_driver_init")
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:8000/account/login/"
    
    def open(self):
        self.driver.get(self.url)
        
    def login(self, email, password):
        self.driver.find_element(By.ID, "id_username").send_keys(email)
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.TAG_NAME, "button").click()

@pytest.mark.usefixtures("chrome_driver_init")     
class TestLogin:
    def test_login_successfull(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.open()
            login_page.login("v@v.com", "Ahoj12345")
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "table"))
            )
                
            expected_url_after_login = "http://localhost:8000/"
            assert self.driver.current_url == expected_url_after_login, f"Expected redirect to {expected_url_after_login}, but got {self.driver.current_url}"
            
            print("Url after login:", self.driver.current_url)
        except StaleElementReferenceException as e:
            print(f"Caught an exception: {e}")