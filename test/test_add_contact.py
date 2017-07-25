# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits +string.punctuation+ " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Contact(firstname="", lastname="", homephone= "",  mobilephone= "", workphone= "", secondphone= "" ,
                 address="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 12), address=random_string("address", 20),
            homephone= random_string("homephone", 10), mobilephone= random_string("mobilephone", 10), workphone= random_string("workphone", 10),
            secondphone= random_string("secondphone", 10) ,email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10))
    for i in range (5)
]

@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname =""))






