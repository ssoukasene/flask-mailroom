import os

from peewee import Model, CharField, DoubleField, ForeignKeyField, DoesNotExist
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class Donor(Model):
    name = CharField(max_length=255, unique=True)

    class Meta:
        database = db

class Donation(Model):
    value = DoubleField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        database = db

