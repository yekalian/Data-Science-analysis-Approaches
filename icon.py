#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""frist program"""
from PyQt5 import QtWidgets, QtGui#载入基本窗口模块,ICON
import sys

class Icon (QtWidgets.QWidget): # notice :
	def __init__(self):
		super().__init__()
        
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,250,150)#set X Y H W
		self.setWindowTitle("inco")
		self.setWindowIcon(QtGui.QIcon(r'E:\xxx.ico'))#set icon


if __name__=='__main__':  #pay attention to __

	app = QtWidgets.QApplication(sys.argv)#application object
	icon = Icon()
	icon.show()#show window of content

sys.exit(app.exec_())# exit