from model.contact import Contact
import random
from model.group import  Group


def test_add_contact_to_group(app,db,orm):
    group=db.get_group_list()
    contact=db.get_contact_list()
    choosen=len(contact)
    if  len(group) ==0 :
        app.group.create(Group(name="New Loop"))
    if len(contact)==0:
        app.contact.create(Contact(firstname="scooby",lastname="lolipop"))
    contacts_to_add=[random.choice(contact) for i in range(random.randrange(choosen))]
    groupp=random.choice(group)

    old_contacts_in_group=orm.get_contacts_in_group(groupp)
    for cont in old_contacts_in_group:
        if cont not in contacts_to_add: contacts_to_add.append(cont)

    new_contacts_in_group=app.contact.add_list_to_group(contacts_to_add, groupp)

    new_contats=sorted(new_contacts_in_group,key=Contact.id_or_max)
    def find_doubles(l):
        n = []
        for i in l:
            if i not in n:
                n.append(i)
        return n

    assert sorted(contacts_to_add,key=Contact.id_or_max)  ==find_doubles(new_contats)

