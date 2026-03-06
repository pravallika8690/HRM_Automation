from test_methods.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # OrangeHRM website elements
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"

    def login_to_app(self, user, pwd):
        self.page.fill(self.username_input, user)
        self.page.fill(self.password_input, pwd)
        self.page.click(self.login_button)

    def logout_from_app(self):
        # 1. ప్రొఫైల్ డ్రాప్‌డౌన్ మీద క్లిక్ చేయడం
        self.page.click(".oxd-userdropdown-name")
        # 2. Logout లింక్ మీద క్లిక్ చేయడం
        self.page.click("text=Logout")
        # 3. లాగిన్ బటన్ కనిపించే వరకు ఆగడం
        self.page.wait_for_selector("button[type='submit']", timeout=10000)