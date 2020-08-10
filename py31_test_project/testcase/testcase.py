import unittest
import os
from py31_test_project.common import myddt
from py31_test_project.common.handle_excel import Operation_excel
from py31_test_project.funcs.login import login_check
from py31_test_project.funcs.register import register
from py31_test_project.common.handle_log import log
from py31_test_project.common.handle_path import DATA_DIR


@myddt.ddt
class Test_case(unittest.TestCase):
    login_excel = Operation_excel(os.path.join(DATA_DIR, 'test_case.xlsx'), 'login')
    login_data_li = login_excel.read_excel()
    register_excel = Operation_excel(os.path.join(DATA_DIR, 'test_case.xlsx'), 'register')
    register_data_li = register_excel.read_excel()

    @myddt.data(*login_data_li)
    def test_login_case(self, case):
        data = eval(case['data'])
        expected = eval(case['expected'])
        actual = login_check(**data)
        row = int(case['case_id'][-3:]) + 1
        title = case['title']
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            self.login_excel.write_excel(row=row, column=5, value='失败')
            log.error(F"{title}:用例执行失败，失败的信息如下")
            log.exception(e)
            raise e
        else:
            self.login_excel.write_excel(row=row, column=5, value='通过')
            log.info(F"{title}:用例执行通过！！！")

    @myddt.data(*register_data_li)
    def test_register_case(self, case):
        data = eval(case['data'])
        expected = eval(case['expected'])
        actual = register(**data)
        row = int(case['case_id'][-3:]) + 1
        title = case['title']
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            self.register_excel.write_excel(row=row, column=5, value='失败')
            # 输出error等级的日志
            log.error(F"{title}:用例执行失败，失败的信息如下")
            # 将异常信息输出到日志，等级为error
            log.exception(e)
            raise e
        else:
            self.register_excel.write_excel(row=row, column=5, value='通过')
            # 输出info等级的日志
            log.info(F"{title}:用例执行通过！！！")


if __name__ == '__main__':
    unittest.main()
