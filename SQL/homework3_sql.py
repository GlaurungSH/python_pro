import sqlite3
from faker import Faker


faker = Faker(['en_US'])


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


def ins_data():
    db = 'homework3.db'
    con = sqlite3.connect(db)
    cur = con.cursor()
    for i in range(10):
        f_name = faker.first_name()
        l_name = faker.last_name()
        addr = faker.address()
        job = faker.job()
        age = faker.random_int(min=0, max=100)
        str_data = (f_name, l_name, addr, job, age)
        sql = f'''
        INSERT INTO person (first_name, last_name, address, job, age)
        VALUES
        {str_data}
        '''
        cur.execute(sql)
        con.commit()
    con.close()


create_person_tb()
ins_data()
