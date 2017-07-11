from model.contact import Contact

def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


#def test_modify_contact_middlename(app):
 #   app.group.modify_first_contact(Contact(middlename="New middlename"))


#def test_modify_contact_lastname(app):
 #   app.group.modify_first_contact(Contact(lastname="New lastname"))


#def test_modify_contact_nickname(app):
 #   app.group.modify_first_contact(Contact(nickname="New nickname"))

