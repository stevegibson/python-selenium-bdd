from framework.webapp import webapp
from selenium.webdriver.common.by import By
class LoginPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
    
    def login(self, user_name, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(user_name)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

login_page = LoginPage.get_instance()