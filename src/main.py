# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

from excel import Excel
from db import Database

try:
    x = Excel("../Data/IPC_Portugal_1977_2013.xls")
    x.read_data()
    lista2 = x.lista

    d = Database(lista2)
    d.drop_table()
    d.create_table()

    d.insert_data()
    d.select('va')

    a = 9.1257182
    a = round(a, 2)
    print '{0:.2f}'.format(a)

except IOError as e:
    print "I/O error ({0}): {1}".format(e.errno, e.strerror)
