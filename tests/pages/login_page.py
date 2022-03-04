from framework.webapp import webapp

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
        self.driver.get("https://www.saucedemo.com")
        # then enter uid/pw and click Login

login_page = LoginPage.get_instance()