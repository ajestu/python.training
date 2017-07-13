from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import session_helper
from fixture.group import Group_helper
from fixture.contact import contactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = session_helper(self)
        self.group = Group_helper(self)
        self.contact = contactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except :
            return  False



    def destroy(self):
        self.wd.quit()