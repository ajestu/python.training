# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app,db,json_groups,check_ui):
    group=json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    old_groups.append(group)
    assert len(old_groups)  == len(db.get_group_list())

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list=list(map(clean,db.get_group_list()))
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max)==sorted(db_list,key=Group.id_or_max)





