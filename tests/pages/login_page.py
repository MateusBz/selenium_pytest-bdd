from pages.base_page import BasePage

from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def set_username(self, username):
        self.find_element(*LoginLocators.username_input).send_keys(username)

    def set_password(self, password):
        self.find_element(*LoginLocators.password_input).send_keys(password)

    def click_login_button(self):
        self.find_element(*LoginLocators.submit_button).click()

    def get_message(self):
        return self.find_element(*LoginLocators.data_msg).text
