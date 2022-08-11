import sys
from PyQt5 import QtPrintSupport,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime


class PrintSupport(QMainWindow):
    """
    使用打印机
    QtPrintSupport
    所有的结果都是以图的形式输出的
    """
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.current = str(datetime.datetime.now().replace(microsecond=0))
        self.current = self.current.replace(':', '-')
        self.editor = QPlainTextEdit(self.current + '\n' + '中科谱康质检仪' + '\n' ,self)
        print(self.editor.currentCharFormat())
        self.editor.setGeometry(20, 60, 260, 200)


    def print(self):
        # 打印对象其实就是一个画布
        printer = QtPrintSupport.QPrinter()
        # 笔
        painter = QPainter()
        painter.begin(printer)  # 以前的参数是self，代表的是绘制到窗口，这里的是打印机
        screen = self.editor.grab()
        painter.drawPixmap(25, 15, screen)
        painter.end()
        print('print')



