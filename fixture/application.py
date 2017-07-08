from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import session_helper
from fixture.group import Group_helper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = session_helper(self)
        self.group = Group_helper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()