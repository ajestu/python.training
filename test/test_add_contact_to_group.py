from model.contact import Contact
import random
from fixture.orm import ORMFixture
from model.group import  Group

db=ORMFixture(host="127.0.0.1", name="addressbook",  user="root", password="")


def test_add_contact_to_group(app,db):
    group=db.get_group_list()
    contact=db.get_contact_list()
    choosen=len(contact)
    if  len(group) ==0 :
        app.group.create(Group(name="New Loop"))
    if len(contact)==0:
        app.contact.create(Contact(firstname="scooby",lastname="lolipop"))
    list_of_contacts=[random.choice(contact) for i in range(random.randrange(choosen))]
    groupp=random.choice(group)
    app.contact.add_list_to_group(list_of_contacts,groupp)
    gr=Group(id=groupp.id,name=groupp.name, header=groupp.header, footer=groupp.footer)
    assert list_of_contacts  == ORMFixture.get_contacts_in_group(gr)