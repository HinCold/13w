from untitled import Ui_Dialog
from PyQt5 import QtCore, QtGui

from PyQt5 import QtWidgets

import sys


class Mywindow(QtWidgets.QMainWindow, Ui_Dialog):

    # 建立的是Main Window项目，故此处导入的是QMainWindow

    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget

    def __init__(self):
        super(Mywindow, self).__init__()

        self.setupUi(self)

    def dclick(self):  # 定义槽函数btn_click(),也可以理解为重载类Ui_MainWindow中的槽函数btn_click()

        self.lineEdit.setText('hhhh')


app = QtWidgets.QApplication(sys.argv)

window = Mywindow()

window.show()

sys.exit(app.exec_())
