# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 下午 14:49
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : operationExcel
# @Software: PyCharm

import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *

class OperationExcel:
	def getExcel(self):
		db=xlrd.open_workbook(data_dir("data","data.xls"))
		sheet=db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取Excel的行数'''
		return self.getExcel().nrows

	def get_row_cel(self,row,col):
		'''获取单元格的内容'''
		return self.getExcel().cell_value(row,col)

	def get_ID(self,row):
		'''获取测试用例ID'''
		return self.get_row_cel(row,getCaseID())

	def get_title(self,row):
		'''获取title'''
		return self.get_row_cel(row, getTitle())

	def getUrl(self,row):
		'''获取请求地址'''
		return self.get_row_cel(row,getUrl())

	def get_request_data(self,row):
		'''获取请求参数'''
		return self.get_row_cel(row, get_request_data())

	def getExpect(self,row):
		'''获取期望结果'''
		return self.get_row_cel(row,getExpect())

	def getResult(self,row):
		'''获取实际的结果'''
		return self.get_row_cel(row,getResult())

	def writeResult(self,row,content):
		'''测试结果写入到文件中'''
		col=getResult()
		work=xlrd.open_workbook(data_dir("data","data.xls"))
		old_content=copy(work)
		ws=old_content.get_sheet(0)
		ws.write(row,col,content)
		old_content.save(data_dir("data","data.xls"))


	def run_success_result(self):
		'''获取执行成功的用例数'''
		pass_count=[]
		fail_count=None
		for i in range(1,self.get_rows()):
			if self.getResult(i)=="pass":
				pass_count.append(i)
		return int(len(pass_count))

	def run_fail_result(self):
		'''获取执行失败的用例数'''
		return int((self.get_rows()-1)-self.run_success_result())

	def run_pass_rate(self):
		'''测试结果通过率'''
		rate=""
		if self.run_fail_result()==0:
			rate="100%"
		elif self.run_fail_result()!=0:
			rate=str(int(self.run_success_result()/int(self.get_rows()-1)*100))+'%'
		return rate







