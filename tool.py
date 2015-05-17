#!/usr/bin/python3
#-*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
import os


class InputDialog(QtWidgets.QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.resize(300, 80)
        grid = QtWidgets.QGridLayout()

        grid.addWidget(QtWidgets.QLabel("请输入文件路径或直接将文件拖入输入框内:"), 1, 0)

        button_ok = QtWidgets.QPushButton("转换")
        grid.addWidget(button_ok, 3, 3)
        button_ok.clicked.connect(self.convert_to_py)

        button_cancel = QtWidgets.QPushButton("退出")
        button_cancel.clicked.connect(self.close)
        grid.addWidget(button_cancel, 3, 4)

        self.line_edit = LineEdit(self)
        grid.addWidget(self.line_edit, 2, 0, 1, 5)

        self.setLayout(grid)

    def convert_to_py(self):
        # 函数用于将designer设计出的.ui文件转化为.py文件
        if self.line_edit.file_path == "":
            QtWidgets.QMessageBox.information(self, "提示", 
                                              "请输入文件路径或者将要转换的文件拖动到文本行中！        ")
            return
        elif self.line_edit.file_suffix.lower() != "ui":
            QtWidgets.QMessageBox.information(self, "提示", 
                                              "该文件不存在或者不是ui文件！        ")
            return
        command = "pyuic5 -o ui_" + self.line_edit.file_name + ".py " + self.line_edit.file_path
        os.popen(command)


# LineEdit是自定义的文字行编辑控件，用于支持相应的拖拽操作
class LineEdit(QtWidgets.QLineEdit):
    file_path = ""
    file_name = ""
    file_suffix = ""

    def __init__(self, parent):
        super(LineEdit, self).__init__(parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.file_path = event.mimeData().urls()[0].url()[8:]
        self.file_name, self.file_suffix = event.mimeData().urls()[0].fileName().rsplit(".", 1)
        self.setText(self.file_path)
        self.parent().convert_to_py()


app = QtWidgets.QApplication(sys.argv)
id = InputDialog()
id.show()
sys.exit(app.exec_())