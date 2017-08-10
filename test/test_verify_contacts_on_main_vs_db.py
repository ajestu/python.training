
import re

def test_verify1(app,db):
    capp=len(db.get_contact_list())
    dbs=app.contact.get_contact_list()

    assert capp==len(dbs)
    for contact in dbs:
        contact_from_home_page = app.contact.get_contact_from_home_page(contact.id )
        contact_from_db = db.get_contact_info_from_db(contact.id)
        assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_db)
        assert clear_email(contact_from_home_page.all_emails) == merge_emails_like_on_home_page(contact_from_db)
      #  assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.id == contact_from_db.id

def clear(s):
    return re.sub("[()/ -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondphone]))))


def clear_email(s):
   para= re.sub("mailto:", "",s)
   return re.sub("[ ]", "",para)



def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))