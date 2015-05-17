#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""状态栏程序"""
import sys
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(0, 150)
        self.setWindowTitle("状态栏程序示例")
        self.statusBar().showMessage("就绪")


if __name__=='__main__':
	
app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())