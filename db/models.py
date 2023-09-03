from mongoengine import Document, CASCADE
from mongoengine.fields import StringField, ListField, ReferenceField


class Authors(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50, required=True)
    born_location = StringField(required=True)
    description = StringField(min_length=10)


class Qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField(min_length=10, unique=True)
    meta = {'allow_inheritance': True}
