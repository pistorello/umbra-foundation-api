from peewee import *

CONN = MySQLDatabase(
    host='localhost',
    database='umbra_foundation',
    user='root',
    password='Metadados01'
)

def startConnection():
    CONN.connect()

def closeConnection():
    if not CONN.is_closed:
        CONN.close