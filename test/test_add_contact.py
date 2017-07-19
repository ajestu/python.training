# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="sdgh", middlename="bsdfg", lastname="sdfghfgg", nickname="xfgh")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    print(old_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname =""))






