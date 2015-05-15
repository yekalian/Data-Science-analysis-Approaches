#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""frist program"""
from PyQt5 import QtWidgets, QtGui#载入基本窗口模块,ICON
import sys

class view (QtWidgets.QWidget): # notice :
	def __init__(self):
		super().__init__()
        
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,250,150)#set X Y H W
		self.setWindowTitle("inco")
		self.setWindowIcon(QtGui.QIcon(r'E:\xxx.ico'))#set icon
		self.setToolTip("This is a <b>QWidget<b> widget")
		QtWidgets.QToolTip.setFont(QtGui.QFont("Times", 10))#set tip
		quit_button = QtWidgets.QPushButton("close",self)#set button
		quit_button.setGeometry(10,10,60,35)#set button postion
		quit_button.clicked.connect(QtWidgets.qApp.quit)#button clicked  connect 

if __name__=='__main__':  #pay attention to __

	app = QtWidgets.QApplication(sys.argv)#application object
	view = view()
	view.show()#show window of content

sys.exit(app.exec_())# exit