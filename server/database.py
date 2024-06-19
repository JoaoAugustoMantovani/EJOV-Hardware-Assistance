import sqlite3

database = sqlite3.connect("ejov-ha.db",timeout=30.0)
cur = database.cursor()

cur.execute('''
            CREATE TABLE Users (
    email TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    birthdate DATE NOT NULL
);
            ''')

database.commit()
database.close()