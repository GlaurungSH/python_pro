import sqlite3
import names
from faker import Faker

def create_person_tb():
    db = 'homework3.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS person(
    personid INTEGER NOT Null PRIMARY KEY AUTOINCREMENT,
    first_name varchar(128) NOT NULL,
    last_name varchar(128) NOT NULL,
    address varchar(1024) NOT NULL,
    job varchar(128) NOT NULL,
    age INTEGER NOT NULL
    )'''
    cur.execute(sql)
    con.close()

create_person_tb()
