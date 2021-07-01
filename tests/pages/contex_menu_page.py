from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.context_menu_locators import ContexMenuLoctors


class ContextMenuPage(BasePage):

    def click_box(self):
        box = self.find_element(*ContexMenuLoctors.box_locator)
        actionChains = ActionChains(self.driver)
        actionChains.context_click(box).perform()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def close_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
