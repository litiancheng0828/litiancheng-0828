import unittest
from unittestreport import TestRunner
from py31_test_project.common.handle_path import CASE_DIR, REPORT_DIR
from py31_test_project.common.handle_config import conf

suite = unittest.defaultTestLoader.discover(CASE_DIR)
runner = TestRunner(suite,
                    filename=conf.get('report', 'filename'),
                    report_dir=REPORT_DIR,
                    title=conf.get('report', 'title'),
                    tester=conf.get('report', 'tester'),
                    desc=conf.get('report', 'desc'),
                    templates=1)
runner.run()
