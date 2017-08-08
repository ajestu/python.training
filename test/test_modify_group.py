from model.group import Group
import random

def test_modify_group_name(app,db,check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    else :
        old_groups = db.get_group_list()
        group= random.choice(old_groups)
        group1=Group(id=group.id,name="fruit loop")
        app.group.modify_group_by_id(group1.id, group)
        assert len(old_groups) == app.group.count()
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        if check_ui:
            assert sorted(map(clean, db.get_group_list()),key=Group.id_or_max)==sorted(app.group.get_group_list(),key=Group.id_or_max)

