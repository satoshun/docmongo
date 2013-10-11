"""
    Defined user table
"""

from docmongo.document import Document
from docmongo.fields import StringField, IntField


class Base(Document):
    _host = "localhost:27017"
    dbname = "test1"


class User(Base):
    fields = {
        "name": StringField,
        "age": IntField
    }
    _get_key = "name"

user = User.get_or_new("sato")
user.age = 100
user.save()

get_user = User.get("sato")
