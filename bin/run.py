# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 下午 15:57
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : run
# @Software: PyCharm

from config.send_mail import *
from config.log import *
from config.HTMLTestRunner import HTMLTestRunner
import unittest

class Runner(object):
	def main_run(self):
		test_dir = os.path.dirname(os.path.dirname(__file__))
		test_report = os.path.join(test_dir, 'report')
		discover = unittest.defaultTestLoader.discover(
			start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests"),
			pattern="test_*.py",
			top_level_dir=None)
		now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
		filename = test_report + '/神农erp测试报告_' + now + '.html'
		fp = open(filename, 'wb')

		# stream放生成报告的路径
		runner = HTMLTestRunner(stream=fp, title="神农erp测试报告", description='用例执行情况：')
		runner.run(discover)
		fp.close()

		new_report = mail_send().new_report(test_report)
		mail_send().send_mail(new_report)
		mail_send()

if __name__ == '__main__':
	Runner().main_run()

