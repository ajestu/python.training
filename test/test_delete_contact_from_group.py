from model.contact import Contact
import random
from model.group import  Group

def test_del_contact_from(app,db,orm):
    group = db.get_group_list()
    contact = db.get_contact_list()
    if len(group)==0 :
        app.group.create(Group(name="HolyLand"))
    if len(contact) == 0:
        app.contact.create(Contact(firstname="new contact"))
    groupp = random.choice(group)
    choosen=orm.get_contacts_in_group(groupp)
    cho_len=len(choosen)
    contacts_to_delete= [random.choice(contact) for i in range(random.randrange(cho_len))]
    new_list_in_group=app.contact.delete_list_from_group(contacts_to_delete,groupp)

    assert len(new_list_in_group) ==len(choosen)-len(contacts_to_delete)
    assert sorted(orm.get_contacts_in_group(group),key=Contact.id_or_max)==sorted(new_list_in_group, key=Contact.id_or_max)