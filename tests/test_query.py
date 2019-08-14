# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 下午 16:14
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : test_logistics
# @Software: PyCharm

import  unittest

from base.method import Method
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

'''demo'''
class XSGL(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.excel=OperationExcel()
		self.operationJson=OperationJson()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['code'], 0)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.obj.isContent(row=row,str2=r.text))



	def test_001(self):
		"采购订单管理"
		# 如果是传data,header="data_form" ，如果传json，header="json"
		#data的内容，放在data目录下的requestData中
		r = self.obj.post(row=1,data=self.operationJson.getRequestsData(row=1),header="data_form")
		print(r.json())
		self.isContent(r=r,row=1)
		self.excel.writeResult(1,"pass")

	def test_002(self):
		"采购计划单管理"
		r = self.obj.post(row=2, data=self.operationJson.getRequestsData(row=2), header="data_form")
		print(r.json())
		self.isContent(r=r, row=2)
		self.excel.writeResult(2, "pass")

	def test_003(self):
		"采购出库管理"
		r = self.obj.post(row=3, data=self.operationJson.getRequestsData(row=3), header="data_form")
		print(r.json())
		self.isContent(r=r, row=3)
		self.excel.writeResult(3, "pass")


