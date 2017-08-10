import re
from model.group import Group
from model.contact import Contact
import mysql.connector

class DbFixture:

    def __init__(self,host,name,user,password):
        self.host=host
        self.name=name
        self.user=user
        self.password= password
        self.connection=mysql.connector.connect(host=host,database=name, user=user,password=password)
        self.connection.autocommit=True

    def get_group_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer)=row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id,firstname,lastname)=row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_info_from_db(self,id):
        contact = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address,email, email2,email3, home,mobile,work,phone2 from addressbook where id=%s "%id)
            for row in cursor:
                (id, firstname, lastname, address,email, email2,email3, home,mobile,work,phone2) =row
                contact.append(Contact(id=str(id), firstname=firstname, lastname=lastname,email=email,email2=email2,email3=email3,homephone=home,mobilephone=mobile, workphone=work,secondphone=phone2
))
        finally:
            cursor.close()
        return contact[0]


    def destroy(self):
        self.connection.close()
