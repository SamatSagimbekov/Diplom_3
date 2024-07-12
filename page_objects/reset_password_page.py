from page_objects.base_page import BasePage
from locators.reset_password_locators import StellarBurgersResetPasswordLocators
from helpers import get_faker_user


class ResetPasswordPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def enter_password(self):
        self.enter_test(StellarBurgersResetPasswordLocators.PASSWORD, get_faker_user()["password"])

    def get_attribute_password(self):
        return str(self.driver.find_element(*StellarBurgersResetPasswordLocators.PASSWORD).get_attribute("type"))

    def click_button_action_password(self):
        self.action_click(StellarBurgersResetPasswordLocators.BUTTON_ACTION_PASSWORD,
                          StellarBurgersResetPasswordLocators.PASSWORD)
