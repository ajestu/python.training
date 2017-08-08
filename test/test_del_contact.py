from model.contact import Contact
import random

def test_delete_first_contact(app,check_ui,db):
    old_contacts=db.get_contact_list()
    if len(old_contacts) == 0 :
        app.contact.create( Contact(firstname="test"))

    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    old_contacts.remove(contact)
    assert len(old_contacts) == app.contact.count()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())

    if check_ui:
        assert sorted(map(clean,old_contacts), key=Contact.id_or_max) ==\
               sorted(app.group.get_contact_list(),  key=Contact.id_or_max)
