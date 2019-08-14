# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 0011 下午 13:43
# @Author  : xuxuchao
# @Email   : 13601208176@139.com
# @File    : send_mail
# @Software: PyCharm


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time,os


class mail_send():

	def send_mail(self,file_new,content=None):
		f = open(file_new, 'rb')
		# 读取测试报告正文
		mail_body = f.read()
		f.close()

		# 发送邮件的
		smtpserver = 'smtp.sina.cn'
		username = '13601208176@sina.cn'
		passwd = '80d357894'
		sender = '13601208176@sina.cn'
		receiver = ['mengxiaowei@ybm100.com','819363280@qq.com','mengxiaowei6@qq.com']
		tname = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
		header = u'%s 接口自动化测试报告 ' % tname

		# 只发正文，不发附件
		msg = MIMEText(mail_body, 'html', 'utf-8')
		msg['Subject'] = Header('自动化测试报告', 'utf-8')
		msg['Header'] = header
		msg['From'] = sender
		msg['To'] = ",".join(receiver)

		# 连接发送邮件
		# 发送邮件,端口用465
		smtp = smtplib.SMTP_SSL(smtpserver, 465)

		smtp.helo(smtpserver)
		smtp.ehlo(smtpserver)
		smtp.login(username, passwd)
		smtp.sendmail(sender, receiver, msg.as_string())
		smtp.quit()

	# ======================查找最新的测试报告==========================

	def new_report(self,testreport):
		dirs = os.listdir(testreport)
		dirs.sort()
		newreportname = dirs[-1]
		# print('The new report name: {0}'.format(newreportname))
		file_new = os.path.join(testreport, newreportname)
		return file_new


