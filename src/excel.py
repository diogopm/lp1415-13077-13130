# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

from mmap import mmap, ACCESS_READ
from xlrd import open_workbook


class Excel:
    excelFileLoc = ""
    workBook = ""
    lista = []

    def __init__(self, excelfilelocation):
        Excel.excelFileLoc = excelfilelocation
        Excel.workBook = open_workbook(Excel.excelFileLoc)
        #print excelfilelocation

    def read_data(self):

        sheet = Excel.workBook.sheet_by_index(0)

        for row in range(1, sheet.nrows):
            lst = []
            for col in range(1, sheet.ncols):
                value = sheet.cell(row, col).value
                if value != '':
                    lst.append(value)
                else:
                    lst.append('NULL')  # não sei se é mesmo assim que se marcam os nulls
            Excel.lista.append(lst)
