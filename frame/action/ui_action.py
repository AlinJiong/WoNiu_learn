class UIAction:

    def __init__(self,driver):
        self.driver = driver


    def login(self, user, password, vcode):
        self.input("username",user)
        self.input("password",password)
        self.input("verifycode",vcode)
        self.driver.find_element_by_css_selector(
            "button.form-control.btn-primary").click()

    def logout(self):
        self.driver.find_element_by_link_text("注销").click()

    def query_product(self, barcode):
        self.input('barcode',barcode)
        self.driver.find_element_by_css_selector(
            'button[onclick="queryByBarCode()"]').click()

    def input(self,locator, content):
        el = self.driver.find_element_by_id(locator)
        el.clear()
        el.send_keys(content)
