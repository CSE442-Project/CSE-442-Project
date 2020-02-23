from selenium.webdriver.support.ui import Select


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title


class IndexPage(BasePage):

    def click_create_client_account_button(self):
        pass

    def click_create_contractor_account_button(self):
        pass
