import sqlite3
from faker import Faker

faker = Faker(['en_US'])
db = 'homework3.db'


def create_person_tb():
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


def print_person():
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = '''
    SELECT last_name, first_name, job, age, personid FROM person ORDER BY last_name
    '''
    person_data = cur.execute(sql)
    for row in person_data:
        print(row)
    con.commit()
    con.close()


def update_person(personid, age):
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = f'''
    UPDATE person
    SET age={age}
    WHERE personid={personid}
    '''
    cur.execute(sql)
    con.commit()
    con.close()


def delete_person(personid):
    con = sqlite3.connect(db)
    cur = con.cursor()
    sql = f'''
    DELETE FROM person
    WHERE personid={personid}
    '''
    cur.execute(sql)
    con.commit()
    con.close()


if __name__ == '__main__':
    create_person_tb()
    ins_data()
    update_person(1, 35)
    delete_person(2)
    print_person()
