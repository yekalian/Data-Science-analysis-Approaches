#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""frist program"""
from PyQt5 import QtWidgets#载入基本窗口模块
import sys

if __name__=='__main__':#注意缩进，判断是否本程序

	app = QtWidgets.QApplication(sys.argv)#application object

	me_window = QtWidgets.QWidget()#用户界面类的父类
	me_window.resize(400,300)#change window size 
	me_window.setWindowTitle("my frist program")# set window title
	me_window.show()#show window of content

sys.exit(app.exec_())# exit