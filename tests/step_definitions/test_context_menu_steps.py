from pytest_bdd import scenario, given, when, then
from pages.base_page import BasePage
from pages.contex_menu_page import ContextMenuPage


@scenario('../features/context_menu.feature', 'Right-click menu')
def test_context_menu(driver_init):
    pass


@given('I go to "context_menu"')
def go_to_context_page(driver_init):
    page = BasePage(driver_init)
    page.visit('context_menu')


@when('I right click in the dotted line box')
def click_box(driver_init):
    ContextMenuPage(driver_init).click_box()


@then('The alert "You selected a context menu" is shown')
def show_alert_text(driver_init):
    assert ContextMenuPage(
        driver_init).get_alert_text() == 'You selected a context menu'
    ContextMenuPage(driver_init).close_alert()
