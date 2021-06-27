from selenium.webdriver.common.by import By


class LoginLocators:
    username_input = (By.CSS_SELECTOR, '#username')
    password_input = (By.CSS_SELECTOR, '#password')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    data_msg = (By.CSS_SELECTOR, '#flash')
