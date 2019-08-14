# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 下午 15:27
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : operationJson
# @Software: PyCharm

import json
from utils.public import *
from utils.operationExcel import OperationExcel

class OperationJson:
	def __init__(self):
		self.excel=OperationExcel()

	def getReadJson(self):
		with open(data_dir(filename="requestData.json"),encoding="utf-8") as fp:
			data=json.load(fp)
			return data

	def getRequestsData(self,row):
		'''获取请求参数'''
		return self.getReadJson()[self.excel.get_request_data(row=row)]
		# return json.dumps(
		# 	self.getReadJson()[self.excel.get_request_data(row=row)]
		# )
