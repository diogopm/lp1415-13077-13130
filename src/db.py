__author__ = 'Diogo'

import sqlite3


class Database:
    db = ''
    data = ''
    cursor = ''

    def __init__(self, data):
        Database.db = sqlite3.connect('test.db')
        Database.data = data
        Database.cursor = Database.db.cursor()

    def drop_table(self):
        Database.cursor.execute('DROP TABLE IPC')
        Database.db.commit()

    def create_table(self):
        Database.cursor.execute(
            ('CREATE TABLE IPC(ano INTEGER PRIMARY KEY, ipc REAL, va REAL, remmax REAL, remmin REAL,\n'
             '    PIBpercap REAL, rnbpca REAL, rdbpca REAL, rpca REAL)'))
        Database.db.commit()

    def insert_data(self):

        for row in Database.data:
            Database.cursor.execute('INSERT INTO IPC VALUES (?,?,?,?,?,?,?,?,?)', row)
        Database.db.commit()

    def test(self):
        Database.cursor.execute('SELECT * FROM IPC')
        for row in Database.cursor:
            print row