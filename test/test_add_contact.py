# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app,json_contacts,check_ui,db):
    contact= json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    old_contacts.append(contact)
    assert len(old_contacts)  == len(db.get_contact_list())

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())

    if check_ui:
        new_contacts=app.contact.get_contact_list()
        db_list = map(clean,old_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







