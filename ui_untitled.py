#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button(QPushButton):
    def __init__(self, image,title, parent):
        super(Button, self).__init__(image,title, parent)

    def style(self): 
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

    def ketPressEvent(self,event):
        if event.key() == Qt.key_Escape:
            self.close()
               
    def uiaction(self):

        self.statusBar()
        exit_menu = QAction(QIcon(r"E:/xxx.ico"), "退出", self)
        exit_menu.setShortcut("Ctrl+Q")
        exit_menu.setStatusTip("退出程序")
        exit_menu.triggered.connect(qApp.quit)



        menubar = self.menuBar()
        file = menubar.addMenu("文件")
        file.addAction(exit_menu)

        self.file_item = QAction(QIcon(r"E:/xx.png"), "打开", self)
        self.file_item.setShortcut("Ctrl+O")
        self.file_item.setStatusTip("打开新文件")
        self.file_item.triggered.connect(self.show_filedialog)

        self.file = self.menuBar().addMenu("文件")
        self.file.addAction(self.file_item)

        self.text_edit = QTextEdit()
        self.text_edit.setGeometry(200,200,200,200)
        self.setCentralWidget(self.text_edit)
        

        self.toolbar = self.addToolBar("退出")
        self.toolbar.addAction(exit_menu)

        

        button1 = Button(QIcon(r"E:/xxx.ico"),"dilog", self)
        button1.setGeometry(110,60,80,50)
        button1.setFocusPolicy(Qt.NoFocus)
        button1.clicked.connect(self.show_dialog)
        self.setFocus()

        button2 = Button(QIcon(r"E:/xxx.ico"),"color", self)
        button2.setGeometry(110,160,80,50)
        button2.setFocusPolicy(Qt.NoFocus)
        button2.clicked.connect(self.show_colordialog)

        color = QColor(0, 0, 0)
        self.widget = QWidget(self)
        self.widget.setStyleSheet("QWidget{background-color:%s}"% color.name())
        self.widget.setGeometry(200, 160, 50, 50)


        button3 = Button(QIcon(r"E:/xxx.ico"),"font", self)
        button3.setGeometry(110,240,80,50)
        button3.setFocusPolicy(Qt.NoFocus)
        button3.clicked.connect(self.show_fontdialog)

        self.label1 = QLabel("普通的disco我们普通的摇", self)
        self.label1.move(200, 240)
        self.h_box = QHBoxLayout()

        self.h_box.addWidget(self.label1, 1)
        self.setLayout(self.h_box)

        

        self.label = QLineEdit(self)
        self.label.move(190, 60)

        lcd = QLCDNumber(self)
        self.slider =QSlider(Qt.Horizontal, self)

        lcd.setGeometry(1,60,100,100)
        self.slider.setGeometry(1,160,100,50)

        self.slider.valueChanged.connect(lcd.display)
        
        self.slider.valueChanged.connect(self.print_value)
        
    def    print_value(self):
        self.tt = self.slider.value()
        cc = str(self.tt)
        print (cc)
        self.label.setText(cc)

    def show_fontdialog(self):

        font, ok = QFontDialog.getFont(self)
        if ok:
            self.label1.setFont(font)

    def show_filedialog(self):
            file_name = QFileDialog.getOpenFileName(self, '打开文件', r"C:\Users\Administrator\Desktop\test/")
            file = open(file_name[0], "r")
            data = file.read()
            self.text_edit.setText(data)
            self.label.setText(data)
        
    def show_colordialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.widget.setStyleSheet("QWidget{background-color:%s}" % col.name())
            self.label1.setStyleSheet("QLabel{Font-color:%s}"% col.name())

    def show_dialog(self):
        text,ok =QInputDialog.getText(self, "输入对话框", "请输入你的名字：")
        if ok:
            self.label.setText(text)
    def style(self):
        with open('window.qss', 'r') as q:
            self.setStyleSheet(q.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main = Main()
    main.show()
    sys.exit(app.exec_())