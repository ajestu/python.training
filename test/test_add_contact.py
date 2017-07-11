# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname ="sdfghd", middlename ="sdghdg", lastname ="sdtyd", nickname ="rtyfghj"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname =""))






