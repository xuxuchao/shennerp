# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 上午 9:31
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : excel_data
# @Software: PyCharm
from http import cookiejar


class ExcelVariable:
	caseID=0
	Title=1
	url=2
	request_data=3
	expect=4
	result=5

def getCaseID():
	return ExcelVariable.caseID

def getTitle():
	return ExcelVariable.Title

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result




