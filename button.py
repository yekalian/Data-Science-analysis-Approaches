#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Button(QPushButton):
	def __init__(self,parent=None):
		super(Button, self).__int__(self,parent)
		with open('window.qss', 'r') as d:
			self.setStyleSheet(d.read())

class QuitButton(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
            
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("我的关闭程序")
        quit_button = Button("关闭", self)
        quit_button.setGeometry(10, 10, 60, 35)
        
        quit_button.clicked.connect(qApp.quit)
        
app = QApplication(sys.argv)
quitbutton = QuitButton()
quitbutton.show()
sys.exit(app.exec_())