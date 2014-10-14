# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

import sqlite3
import types


class Database:
    db = ''
    data = ''
    cursor = ''

    def __init__(self, data):
        Database.db = sqlite3.connect('test.db')
        Database.data = data
        Database.cursor = Database.db.cursor()

    def drop_table(self):

        Database.cursor.execute('DROP TABLE IF EXISTS IPC')
        Database.db.commit()

    def create_table(self):

        Database.cursor.execute(
            ('CREATE TABLE IF NOT EXISTS IPC(ano INTEGER PRIMARY KEY, ipc REAL, va REAL, remmax REAL, remmin REAL,\n'
             '    PIBpercap REAL, rnbpca REAL, rdbpca REAL, rpca REAL)'))
        Database.db.commit()

    def insert_data(self):

        for row in Database.data:
            Database.cursor.execute('INSERT INTO IPC VALUES (?,?,?,?,?,?,?,?,?)', row)
        Database.db.commit()

    def test(self):
        Database.cursor.execute('SELECT * FROM IPC')
        for row in Database.cursor:
            #print row
            for value in row:
                print value,
            print

    def select(self, attrb):
        Database.cursor.execute('SELECT ' + attrb + ' FROM IPC')
        Database.db.commit()
        for row in Database.cursor:
            for value in row:
                if isinstance(value, float):
                    #print '{0:.2f}'.format(value), # acho que não vale a pena usar este
                    print float(round(value, 2)),
                else:
                    print value,
            print
