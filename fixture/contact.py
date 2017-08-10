import re
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
        if not (wd.current_url.endswith("index.php") or wd.current_url.endswith("addressbook/")):
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()
        self.contact_cashe = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell =row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contacts_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contacts_view_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_element_by_id(id)
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

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

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        chk= wd.find_element_by_xpath('//input[@id="%s"]'%id)
        row=chk.find_element_by_xpath("./../..")
        cells=row.find_elements_by_css_selector("td")
        cells[7].click()


    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondphone)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

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
            self.app.open_home_page()
            self.contact_cashe = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails=cells[4].text
                address=cells[3].text
                self.contact_cashe.append(Contact(firstname = firstname, lastname = lastname, id = id,
                                                  all_phones_from_homepage=all_phones,address=address,all_emails=all_emails ))
        return list(self.contact_cashe)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def get_contact_from_home_page(self,id):
            wd = self.app.wd
            self.app.open_home_page()
            chk = wd.find_element_by_xpath('//input[@id="%s"][@name="selected[]"]' % id)
            row = chk.find_element_by_xpath("./../..")
            cells = row.find_elements_by_css_selector("td")
            firstname = cells[2].text
            lastname = cells[1].text
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            all_phones = cells[5].text
            all_emails=cells[4].text
            address=cells[3].text
            return Contact(firstname = firstname, lastname = lastname, id = id,
                                          all_phones_from_homepage=all_phones,address=address,all_emails=all_emails )

    #[ @ name = "selected[]"]

    def get_contact_info_from_edit_page(self, index):
        wd=self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        address=wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname = firstname, lastname = lastname, id=id, homephone=homephone, workphone=workphone,
                        mobilephone=mobilephone, secondphone=secondphone, address=address, email=email,email2=email2,email3=email3)

    def get_contact_from_view_page(self, index):
        wd=self.app.wd
        self.open_contacts_view_by_index(index)
        text=wd.find_element_by_id("content").text
        homephone=re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondphone=secondphone)
