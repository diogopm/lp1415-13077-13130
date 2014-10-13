# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

from excel import Excel
from db import Database

x = Excel("../Data/IPC_Portugal_1977_2013.xls")
x.read_data()
lista2 = x.lista2

d = Database(lista2)
d.drop_table()
d.create_table()

d.insert_data()

d.test()