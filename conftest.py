import pytest
import time
from pytest_factoryboy import register
from tests.factories import UserFactory
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

register(UserFactory)

@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=800,600")
    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = chrome_driver
    yield
    time.sleep(2)
    chrome_driver.quit()
    

    
    