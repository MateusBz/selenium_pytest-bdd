class BasePage:

    def __init__(self, driver, base_url='https://the-internet.herokuapp.com/'):
        self.driver = driver
        self.base_url = base_url

    def visit(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def find_element(self, *locators):
        return self.driver.find_element(*locators)
