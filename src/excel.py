# -*- coding: utf-8 -*-
# authors 13077/13130
# data: 05 de outubro de 2014
#

from mmap import mmap, ACCESS_READ
from xlrd import open_workbook


class Excel:
    excelFileLoc = ""
    workBook = ""
    lista = [[[]]]
    lista2 = []

    def __init__(self, excelfilelocation):
        Excel.excelFileLoc = excelfilelocation
        print excelfilelocation

    def readFile(self):

        Excel.workBook = open_workbook(Excel.excelFileLoc)
        x = 0
        y = 0
        for s in Excel.workBook.sheets():
            print 'Sheet:', s.name
            if x == 0:
                for row in range(s.nrows):
                    Excel.lista[x].append([])
                    for col in range(s.ncols):
                        Excel.lista[x][y].append(s.cell(row, col).value)
                    y += 1
            x += 1

    def read_data(self):
        Excel.workBook = open_workbook(Excel.excelFileLoc)
        sheet = Excel.workBook.sheet_by_index(0)

        for row in range(1, sheet.nrows):
            lst = []
            for col in range(1, sheet.ncols):
                value = sheet.cell(row, col).value
                if value != '':
                    lst.append(value)
                else:
                    lst.append('null')  # não sei se é mesmo assim que se marcam os nulls
            Excel.lista2.append(lst)

