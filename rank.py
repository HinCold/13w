# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rank.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_p(object):
    def setupUi(self, p):
        p.setObjectName("p")
        p.resize(1039, 757)
        p.setMinimumSize(QtCore.QSize(1039, 757))
        p.setMaximumSize(QtCore.QSize(1039, 757))
        p.setStyleSheet("QDialog#p {\n"
"    \n"
"    border-image: url(:/新前缀/images/QQ图片20191010185645.jpg);\n"
"}")
        self.frame = QtWidgets.QFrame(p)
        self.frame.setGeometry(QtCore.QRect(200, 50, 661, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(170, 30, 271, 91))
        self.graphicsView.setStyleSheet("border-image: url(:/新前缀/images/1 (2).png);")
        self.graphicsView.setObjectName("graphicsView")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 150, 551, 81))
        self.frame_2.setStyleSheet("QFrame#frame_2 {\n"
"    \n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid #FFFFFF 2px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(40, 240, 551, 331))
        self.frame_3.setStyleSheet("QFrame#frame_3 {\n"
"    \n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    border: 2px solid #FFFFFF 2px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rank2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rank2.setFont(font)
        self.rank2.setText("")
        self.rank2.setAlignment(QtCore.Qt.AlignCenter)
        self.rank2.setObjectName("rank2")
        self.gridLayout.addWidget(self.rank2, 2, 1, 1, 1)
        self.id3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.id3.setFont(font)
        self.id3.setText("")
        self.id3.setAlignment(QtCore.Qt.AlignCenter)
        self.id3.setObjectName("id3")
        self.gridLayout.addWidget(self.id3, 3, 2, 1, 1)
        self.id4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.id4.setFont(font)
        self.id4.setText("")
        self.id4.setAlignment(QtCore.Qt.AlignCenter)
        self.id4.setObjectName("id4")
        self.gridLayout.addWidget(self.id4, 4, 2, 1, 1)
        self.id1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.id1.setFont(font)
        self.id1.setStyleSheet("color: rgb(170, 0, 0);")
        self.id1.setText("")
        self.id1.setAlignment(QtCore.Qt.AlignCenter)
        self.id1.setObjectName("id1")
        self.gridLayout.addWidget(self.id1, 0, 2, 1, 1)
        self.id2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.id2.setFont(font)
        self.id2.setText("")
        self.id2.setAlignment(QtCore.Qt.AlignCenter)
        self.id2.setObjectName("id2")
        self.gridLayout.addWidget(self.id2, 2, 2, 1, 1)
        self.rank3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rank3.setFont(font)
        self.rank3.setText("")
        self.rank3.setAlignment(QtCore.Qt.AlignCenter)
        self.rank3.setObjectName("rank3")
        self.gridLayout.addWidget(self.rank3, 3, 1, 1, 1)
        self.rank4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rank4.setFont(font)
        self.rank4.setText("")
        self.rank4.setAlignment(QtCore.Qt.AlignCenter)
        self.rank4.setObjectName("rank4")
        self.gridLayout.addWidget(self.rank4, 4, 1, 1, 1)
        self.rank1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rank1.setFont(font)
        self.rank1.setStyleSheet("color: rgb(170, 0, 0);")
        self.rank1.setText("")
        self.rank1.setAlignment(QtCore.Qt.AlignCenter)
        self.rank1.setObjectName("rank1")
        self.gridLayout.addWidget(self.rank1, 0, 1, 1, 1)
        self.point1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.point1.setFont(font)
        self.point1.setStyleSheet("color: rgb(170, 0, 0);")
        self.point1.setText("")
        self.point1.setAlignment(QtCore.Qt.AlignCenter)
        self.point1.setObjectName("point1")
        self.gridLayout.addWidget(self.point1, 0, 3, 1, 1)
        self.point2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.point2.setFont(font)
        self.point2.setText("")
        self.point2.setAlignment(QtCore.Qt.AlignCenter)
        self.point2.setObjectName("point2")
        self.gridLayout.addWidget(self.point2, 2, 3, 1, 1)
        self.point3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.point3.setFont(font)
        self.point3.setText("")
        self.point3.setAlignment(QtCore.Qt.AlignCenter)
        self.point3.setObjectName("point3")
        self.gridLayout.addWidget(self.point3, 3, 3, 1, 1)
        self.point4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.point4.setFont(font)
        self.point4.setText("")
        self.point4.setAlignment(QtCore.Qt.AlignCenter)
        self.point4.setObjectName("point4")
        self.gridLayout.addWidget(self.point4, 4, 3, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 290, 251, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(p)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 51, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(p)
        self.pushButton_4.clicked.connect(p.goback)
        self.pushButton_2.clicked.connect(p.nextpage)
        self.pushButton_3.clicked.connect(p.frontpage)
        QtCore.QMetaObject.connectSlotsByName(p)

    def retranslateUi(self, p):
        _translate = QtCore.QCoreApplication.translate
        p.setWindowTitle(_translate("p", "Dialog"))
        self.label.setText(_translate("p", "排名"))
        self.label_2.setText(_translate("p", "用户名"))
        self.label_3.setText(_translate("p", "积分"))
        self.pushButton_3.setText(_translate("p", "上一页<<<"))
        self.label_4.setText(_translate("p", "1"))
        self.pushButton_2.setText(_translate("p", ">>>下一页"))
        self.pushButton_4.setText(_translate("p", "<"))
import loginimg_rc
