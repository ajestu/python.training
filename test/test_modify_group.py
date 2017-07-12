from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        app.group.modify(Group(name="New name"))
    else:
        app.group.delete_first_group()

#def test_modify_group_header(app):
 #   app.group.modify(Group(header="New header"))


#def test_modify_group_footer(app):
 #   app.group.modify(Group(footer="New footer"))
