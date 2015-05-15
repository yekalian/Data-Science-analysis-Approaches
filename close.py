#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""frist program"""
from PyQt5 import QtWidgets, QtGui#载入基本窗口模块,ICON
import sys

class MainWindow(QtWidgets.QMainWindow):
		def __init__(self):
			super(MainWindow, self).__init__()

			self.status()

		def status(self):
			self.statusBar().showMessage("就绪")


class view (QtWidgets.QWidget): # notice :
	def __init__(self):
		super(view,self).__init__()
		self.MainWindow=MainWindow()
		self.MainWindow.status
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,250,150)#set X Y H W
		self.setWindowTitle("inco")
		self.setWindowIcon(QtGui.QIcon(r'E:\xxx.ico'))#set icon
		self.setToolTip("This is a <b>QWidget<b> widget")
		QtWidgets.QToolTip.setFont(QtGui.QFont("Times", 10))#set tip
		quit_button = QtWidgets.QPushButton("close",self)#set button
		quit_button.setGeometry(10,10,60,35)#set button postion
		quit_button.clicked.connect(self.closeEvent)#button clicked  connect 
		screen =QtWidgets.QDesktopWidget().screenGeometry()#screen center
		size =self.geometry()
		self.move((screen.width()- size.width())/2, (screen.height() - size.height())/2)
	def closeEvent(self,event):
		reply = QtWidgets.QMessageBox.question(self,'ensure quit','Are you sure quit?',
		                                       QtWidgets.QMessageBox.Yes,
		                                       QtWidgets.QMessageBox.No)

		if reply == QtWidgets.QMessageBox.Yes:
			event.accpet()

		else:
			event.ignore()
	




if __name__=='__main__':  #pay attention to __

	app = QtWidgets.QApplication(sys.argv)#application object
	
	view = view()
	view.show()#show window of content

sys.exit(app.exec_())# exit