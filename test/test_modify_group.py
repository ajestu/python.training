from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
        app.group.modify(Group(name="New name"))
        app.group.delete_first_group()
    else :
        old_groups = app.group.get_group_list()
        group = Group(name="New Group")
        group.id = old_groups[0].id
        app.group.modify(group)
        assert len(old_groups) == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#def test_modify_group_header(app):
 #   app.group.modify(Group(header="New header"))


#def test_modify_group_footer(app):
 #   app.group.modify(Group(footer="New footer"))
