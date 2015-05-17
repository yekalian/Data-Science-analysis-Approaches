#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button(QPushButton):
    def __init__(self, image,title, parent):
        super(Button, self).__init__(image,title, parent)

    def style(): 
        with open('window1.qss', 'r') as d:
            self.setStyleSheet(d.read())
                 
class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        grid = QGridLayout()
        self.setObjectName('main')
        self.setWindowTitle('Hello Qt')
        self.setWindowIcon(QIcon('E:/xx.jpg'))
        self.resize(500, 500)
        
        self.uiaction()
       
        self.style()

    def uiaction(self):

        self.statusBar()
        exit_menu = QAction(QIcon(r"E:/xxx.ico"), "退出", self)
        exit_menu.setShortcut("Ctrl+Q")
        exit_menu.setStatusTip("退出程序")
        exit_menu.triggered.connect(qApp.quit)



        menubar = self.menuBar()
        file = menubar.addMenu("文件")
        file.addAction(exit_menu)

        menubar = self.menuBar()
        file = menubar.addMenu("文件")
        file.addAction(exit_menu)

        self.toolbar = self.addToolBar("退出")
        self.toolbar.addAction(exit_menu)

        self.toolbar = self.addToolBar("退出")
        self.toolbar.addAction(exit_menu)

        button = Button(QIcon(r"E:/xxx.ico"),"按钮", self)
        button.move(170, 65)
        button.resize(10,10)

        buttton_names = ['Cls', 'Bck', '', 'Close',
                         '7', '8', '9', '/',
                         '4', '5', '6', '*',
                         '1', '2', '3', '-',
                         '0', '.', '=', '+']
        main_ground = QWidget()
        self.setCentralWidget(main_ground)
        grid = QGridLayout()

        lcd = QLCDNumber(self)
        lcd.resize(10,10)
        slider = QSlider(Qt.Horizontal, self)
        slider.resize(10,10)
        for [n, (x, y)] in enumerate([(i, j) for i in range(5) for j in range(4)]):
            if (x, y) == (0, 2):
                grid.addWidget(QLabel(buttton_names[n]), x, y,1,1)
            if (x,y) ==(2,2):
                
                grid.addWidget(lcd, 1, 1)
            if (x,y) ==(3,3):
                
                grid.addWidget(slider, 4, 4)
            else:
                buttons=QPushButton(QIcon(r"E:/xxx.ico"),buttton_names[n])
                buttons.resize(10,10)
               
                         
        


        
        slider.valueChanged.connect(lcd.display)
        main_ground.setLayout(grid)
     

      

    def style(self):
        with open('window.qss', 'r') as q:
            self.setStyleSheet(q.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main = Main()
    main.show()
    sys.exit(app.exec_())