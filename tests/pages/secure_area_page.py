from pages.base_page import BasePage
from locators.secure_area_locators import SecureAreaLocators


class SecureAreaPage(BasePage):

    def get_message(self):
        return self.find_element(*SecureAreaLocators.data_msg).text
