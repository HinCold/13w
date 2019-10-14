# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1039, 757)
        Dialog.setMinimumSize(QtCore.QSize(1039, 757))
        Dialog.setMaximumSize(QtCore.QSize(1039, 757))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog#Dialog {\n"
"    \n"
"    border-image: url(:/新前缀/images/E9228FE3C623A0A7F60A961D6A4E1304.jpg);\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(230, 60, 581, 571))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(140, 220, 311, 81))
        self.frame_2.setStyleSheet("QFrame#frame_2 {\n"
"    \n"
"    border-image: url(:/新前缀/images/menubt.png);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.game = QtWidgets.QPushButton(self.frame_2)
        self.game.setGeometry(QtCore.QRect(70, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.game.setFont(font)
        self.game.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.game.setObjectName("game")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 20, 51, 41))
        self.pushButton_2.setStyleSheet("border-image: url(:/新前缀/images/mnbt.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(140, 300, 311, 81))
        self.frame_3.setStyleSheet("QFrame#frame_3 {\n"
"    \n"
"    border-image: url(:/新前缀/images/menubt.png);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.rank = QtWidgets.QPushButton(self.frame_3)
        self.rank.setGeometry(QtCore.QRect(70, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rank.setFont(font)
        self.rank.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.rank.setObjectName("rank")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 20, 51, 41))
        self.pushButton_5.setStyleSheet("border-image: url(:/新前缀/images/mnbt.png);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(80, 50, 411, 121))
        self.graphicsView.setStyleSheet("border-image: url(:/新前缀/images/QQ截图20191011220153.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(140, 380, 311, 81))
        self.frame_4.setStyleSheet("QFrame#frame_4 {\n"
"    \n"
"    border-image: url(:/新前缀/images/menubt.png);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.rank_2 = QtWidgets.QPushButton(self.frame_4)
        self.rank_2.setGeometry(QtCore.QRect(70, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rank_2.setFont(font)
        self.rank_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.rank_2.setObjectName("rank_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 20, 51, 41))
        self.pushButton_6.setStyleSheet("border-image: url(:/新前缀/images/mnbt.png);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame5 = QtWidgets.QGraphicsView(self.frame)
        self.frame5.setGeometry(QtCore.QRect(140, 460, 311, 81))
        self.frame5.setStyleSheet("border-image: url(:/新前缀/images/menubt.png);\n"
"")
        self.frame5.setObjectName("frame5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(170, 480, 51, 41))
        self.pushButton.setStyleSheet("border-image: url(:/新前缀/images/mnbt.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 470, 181, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.rank.clicked.connect(Dialog.showrank)
        self.rank_2.clicked.connect(Dialog.history)
        self.game.clicked.connect(Dialog.showdj)
        self.pushButton_3.clicked.connect(Dialog.show_login)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.game.setText(_translate("Dialog", "开始游戏"))
        self.rank.setText(_translate("Dialog", "排行榜"))
        self.rank_2.setText(_translate("Dialog", "历史对局"))
        self.pushButton_3.setText(_translate("Dialog", "退出游戏"))
import loginimg_rc
