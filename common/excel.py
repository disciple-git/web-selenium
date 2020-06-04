import xlrd
from common import read_config
from log import  log


class ReadExcel:
    def __init__(self):
        rc = read_config.ReadConfig('path.ini')
        path = rc.get_db('testdata', 'path')
        sheetname = rc.get_db('testdata', 'sheetname')
        self.logger = log.Logger()
        self.book = self.open_excel(path)
        self.sheet = self.book.sheet_by_name(sheetname)

    def open_excel(self, path):
        try:
            book = xlrd.open_workbook(path)
            return book
        except(Exception):
            self.logger.error("打开excel文件失败")

    def get_lines(self):
        lines = self.sheet.nrows
        return lines

    def get_cell(self, row, col):
        value = self.sheet.cell_value(row, col)
        return value


if __name__ == '__main__':
    value = ReadExcel().get_cell(2, 3)
    print(value)