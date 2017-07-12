from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
        app.group.modify_first_contact(Contact(firstname= "New firstlename"))
    else:
        app.contact.delete_first_contact()
        
#def test_modify_contact_middlename(app):
 #   app.group.modify_first_contact(Contact(middlename="New middlename"))


#def test_modify_contact_lastname(app):
 #   app.group.modify_first_contact(Contact(lastname="New lastname"))


#def test_modify_contact_nickname(app):
 #   app.group.modify_first_contact(Contact(nickname="New nickname"))

