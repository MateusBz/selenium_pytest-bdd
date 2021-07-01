from pytest_bdd import scenario, given, when, then
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from selenium.common.exceptions import NoSuchElementException


@scenario('../features/form_auth.feature', 'Logging test')
def test_error_message(driver_init):
    pass


@given('I go to "login"')
def go_to_login_page(driver_init):
    page = BasePage(driver_init)
    page.visit('login')


@when('I enter <user_name> into "Username" input')
def get_username(driver_init, user_name):
    LoginPage(driver_init).set_username(user_name)


@when('I enter <password> into "Password" input')
def get_password(driver_init, password):
    LoginPage(driver_init).set_password(password)


@when('I click on "Login"')
def log_into_account(driver_init):
    login_button = LoginPage(driver_init)
    login_button.click_login_button()


@then('<message> is shown')
def get_error_message(driver_init, message):
    try:
        if message == 'You logged into a secure area!':
            e_message = SecureAreaPage(driver_init).get_message()
        else:
            e_message = LoginPage(driver_init).get_message()
    except NoSuchElementException:
        pass
    assert e_message.replace('\n×', '') == message
