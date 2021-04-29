import unittest
import os

import HTMLTestRunner

case_path = os.path.join(os.getcwd(), 'testcase')
suite = unittest.defaultTestLoader.discover(case_path, '*ui*')
with open('report/report.html', 'w', encoding='utf-8') as f:
    runner = HTMLTestRunner.HTMLTestRunner(f, title='woniusales test report', verbosity=2)
    runner.run(suite)
