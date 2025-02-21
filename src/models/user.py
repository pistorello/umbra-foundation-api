# MODEL

from peewee import *
import datetime
import db_connection

class Users(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=100, unique=True)
    password = BlobField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_connection.CONN