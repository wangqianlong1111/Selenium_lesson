import testsuites.test_baidu
import testsuites.test_baidu_new
import unittest
import getcwd
import os
import HTMLTestRunnerCN
from framework.my_email import mail

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testsuites.test_baidu.test_baidu('test_baisu'))
    suite.addTest(testsuites.test_baidu_new.test_baidu_new('test_new'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path,'report/xxxUI自动化测试报告.html')
    fp = open(file_path,'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream = fp,
        title = 'xxxUI自动化测试报告',
        description = '报告中描述部分',
        tester = '测试者'
    )
    runner.run(suite)
    fp.close()
    mail()

