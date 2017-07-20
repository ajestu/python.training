from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
        app.contact.modify_first_contact(Contact(firstname= "New firstlename"))
        app.contact.delete_first_contact()
    else:
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="New contact")
        contact.id = old_contacts[0].id
        app.contact.modify_first_contact(contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[0] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
 #   app.group.modify_first_contact(Contact(middlename="New middlename"))


#def test_modify_contact_lastname(app):
 #   app.group.modify_first_contact(Contact(lastname="New lastname"))


#def test_modify_contact_nickname(app):
 #   app.group.modify_first_contact(Contact(nickname="New nickname"))

