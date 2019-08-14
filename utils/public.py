# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 0004 上午 11:11
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : public
# @Software: PyCharm

import os

def data_dir(data="data",filename=None):
	'''查找文件的路径'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,filename)