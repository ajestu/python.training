from model.group import Group

def test_modify_group_name(app):
    app.group.modify(Group(name="New name"))

def test_modify_group_header(app):
    app.group.modify(Group(header="New header"))


#def test_modify_group_footer(app):
 #   app.group.modify(Group(footer="New footer"))
