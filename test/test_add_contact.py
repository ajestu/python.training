# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname ="sdfghd", middlename ="sdghdg", lastname ="sdtyd", nickname ="rtyfghj"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname =""))
    app.session.logout()





