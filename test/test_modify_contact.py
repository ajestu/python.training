from model.contact import Contact
import random

def test_modify_contact(app,db,check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    else:
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
        contact1 = Contact(id=contact.id, firstname="new name")
        app.contact.modify_contact_by_id(contact1.id, contact1)
        assert len(old_contacts) == app.contact.count()
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.name.strip())
        if check_ui:
            assert sorted(map(clean, db.get_contact_list()),key=Contact.id_or_max)==sorted(app.contact.get_contact_list(),key=Contact.id_or_max)




