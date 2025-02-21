# MODEL

from peewee import *
import db_connection
import datetime

class Entities(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=200)
    description = TextField()
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_connection.CONN