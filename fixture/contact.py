from model.contact import Contact

class contactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.add_contact()
        self.fill_contact_form(contact)
        #submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_contacts_page()
        self.contact_cashe = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") or wd.current_url.endswith("localhost/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index( 0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cashe = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self,index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index )
        # open modification form
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contact_cashe = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cashe= []
            for element in wd.find_elements_by_css_selector( "tr[name='entry']"):
                cells = element.find_elements_by_css_selector("td")
                text= cells[2].text
                id = cells[0].find_element_by_css_selector("input").get_attribute("value")
                self.contact_cashe.append(Contact( id=id, firstname= text ))
        return list(self.contact_cashe)



