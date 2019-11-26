from common.excel import ReadExcel
from page.basedriver import BaseDriver
import time


class TestCase:
    def run_main(self):
        self.handle_excel = ReadExcel()
        self.action_method = BaseDriver()
        time.sleep(2)
        case_lines = self.handle_excel.get_lines()
        for i in range(1, case_lines):
            is_run = self.handle_excel.get_cell(i, 2)
            if is_run == 'yes':
                method = self.handle_excel.get_cell(i, 3)
                handle_value = self.handle_excel.get_cell(i, 4)
                send_value = self.handle_excel.get_cell(i, 5)
                if send_value == '':
                    if handle_value == '':
                        self.run_method(method)
                    else:
                        self.run_method(method, handle_value)
                else:
                    self.run_method(method, handle_value, send_value)
            time.sleep(1)

    def run_method(self, method, handle_value=None, send_value=None):
        action_function = getattr(self.action_method, method)
        if send_value==None:
            if handle_value==None:
                action_function()
            else:
                action_function(handle_value)
        else:
            action_function(handle_value, send_value)


if __name__ == '__main__':
    TestCase().run_main()
