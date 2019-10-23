import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import login1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
from httpfunction import *
import history
import rank
import game
import menu

class Mywindow(QtWidgets.QDialog, login1.Ui_Dialog):
    '''
    封装登录界面的ui的类 login.uialog
    这样直接在这个类中定义槽函数 就能连接到之前在designer里设置的信号槽，
    就是按按钮有响应了
    '''
    # 初始化 加载界面
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.login = True

    # 登录按钮的槽函数
    def b_login(self):
        # print('aaaaaaaaaaa')
        if self.login:
            '''
            login post
            '''
            paw = self.lineEdit.text()
            user = self.lineEdit_3.text()
            if not paw == '' and not user == '':
                status, pid = login(user, paw)
                if status == 0:
                    self.hide()
                    w = winmenu(window)
                    w.setFixedSize(1039, 757)
                    # w.move(100, 100)
                    w.show()
                else:
                    print('username or password is wrong!')
            else:
                print('please input username and password!')
        else:
            '''
            register
            '''
            paw = self.lineEdit.text()
            user = self.lineEdit_3.text()

            if not paw == '' and not user == '':
                status, pid = register(user, paw)

                if status:
                    '''
                    以下函数达到切换页面效果
                    即关闭当前窗口 对新的想要的界面实例化
                    然后show出来
                    '''
                    self.hide()
                    w = winmenu(window)
                    w.setFixedSize(1039, 757)
                    # w.move(100, 100)
                    w.show()
                else:
                    print('Username already registered!')
            else:
                print('please input username and password!')
    # 注册按钮槽函数
    def register(self):
        if self.login:
            self.login = False

            self.label.setText('register')
            self.pushButton.setText('注册并登入')
            self.pushButton_2.setText('返回')
        else:
            self.login = True

            self.label.setText('log on')
            self.pushButton.setText('登录')
            self.pushButton_2.setText('注册')


class winmenu(QtWidgets.QDialog, menu.Ui_Dialog):
    '''
    与上面相同，封装菜单界面ui
    '''
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)
    # 返回登录界面槽函数 即注销
    def show_login(self):

        logout(header)
        self.hide()
        window.show()
        window.setFixedSize(1039, 757)
        self.close()
    # 排行榜槽函数
    def showrank(self):
        self.close()


        w = winrank(window)

        w.setFixedSize(1039, 757)
        # w.move(100, 100)
        w.show()
    #开始游戏槽函数
    def showgame(self):
        self.close()

        w = wingame(window)

        w.setFixedSize(1039, 757)
        # w.move(100, 100)
        w.show()
    # 历史记录槽函数
    def history(self):


        self.close()

        w = winhistory(window)

        w.setFixedSize(1039, 757)
        # w.move(100, 100)

        w.show()


class winrank(QtWidgets.QDialog, rank.Ui_p):
    '''
    排行榜
    '''
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.page = 1
        self.setupUi(self)

        self.res = httprank(header)
        self.long = len(self.res)/4
        print(self.res)
        print(self.res[(self.page - 1) * 4]['player_id'])
        quece = (self.page-1)*4 + 1
        self.rank1.setText('No.{}'.format(quece))
        self.rank2.setText('No.{}'.format(quece+1))
        self.rank3.setText('No.{}'.format(quece+2))
        self.rank4.setText('No.{}'.format(quece+3))
        self.id1.setText(str(self.res[(self.page - 1) * 4]['name']))
        self.id2.setText(str(self.res[(self.page - 1) * 4 + 1]['name']))
        self.id3.setText(str(self.res[(self.page - 1) * 4 + 2]['name']))
        self.id4.setText(str(self.res[(self.page - 1) * 4 + 3]['name']))
        self.point1.setText(str(self.res[(self.page - 1) * 4]['score']))
        self.point2.setText(str(self.res[(self.page - 1) * 4 + 1]['score']))
        self.point3.setText(str(self.res[(self.page - 1) * 4 + 2]['score']))
        self.point4.setText(str(self.res[(self.page - 1) * 4 + 3]['score']))

    def nextpage(self):
        if self.page < self.long:
            self.page += 1
            quece = (self.page - 1) * 4 + 1
            self.label_4.setText(str(self.page))
            self.rank1.setText('No.{}'.format(quece))
            self.rank2.setText('No.{}'.format(quece + 1))
            self.rank3.setText('No.{}'.format(quece + 2))
            self.rank4.setText('No.{}'.format(quece + 3))
            self.id1.setText(str(self.res[(self.page - 1) * 4]['name']))
            self.id2.setText(str(self.res[(self.page - 1) * 4 + 1]['name']))
            self.id3.setText(str(self.res[(self.page - 1) * 4 + 2]['name']))
            self.id4.setText(str(self.res[(self.page - 1) * 4 + 3]['name']))
            self.point1.setText(str(self.res[(self.page - 1) * 4]['score']))
            self.point2.setText(str(self.res[(self.page - 1) * 4 + 1]['score']))
            self.point3.setText(str(self.res[(self.page - 1) * 4 + 2]['score']))
            self.point4.setText(str(self.res[(self.page - 1) * 4 + 3]['score']))
    def frontpage(self):
        if self.page > 1:
            self.page -= 1
            quece = (self.page - 1) * 4 + 1
            self.label_4.setText(str(self.page))
            self.rank1.setText('No.{}'.format(quece))
            self.rank2.setText('No.{}'.format(quece + 1))
            self.rank3.setText('No.{}'.format(quece + 2))
            self.rank4.setText('No.{}'.format(quece + 3))
            self.id1.setText(str(self.res[(self.page - 1) * 4]['name']))
            self.id2.setText(str(self.res[(self.page - 1) * 4 + 1]['name']))
            self.id3.setText(str(self.res[(self.page - 1) * 4 + 2]['name']))
            self.id4.setText(str(self.res[(self.page - 1) * 4 + 3]['name']))
            self.point1.setText(str(self.res[(self.page - 1) * 4]['score']))
            self.point2.setText(str(self.res[(self.page - 1) * 4 + 1]['score']))
            self.point3.setText(str(self.res[(self.page - 1) * 4 + 2]['score']))
            self.point4.setText(str(self.res[(self.page - 1) * 4 + 3]['score']))
    # 返回按钮
    def goback(self):
        self.close()
        menuPale = winmenu(window)
        menuPale.setFixedSize(1039, 757)
        menuPale.show()


class wingame(QtWidgets.QMainWindow, game.Ui_MainWindow):
    '''
    与上面相同，封装菜单界面ui
    '''
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)
    # 返回菜单界面槽函数 即注销
    def backmenu(self):
        self.close()
        menuPale = winmenu(window)
        menuPale.setFixedSize(1039, 757)
        # menuPale.resize(1039, 757)
        menuPale.show()

class winhistory(QtWidgets.QDialog, history.Ui_Dialog):
    '''
    历史
    '''
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)
        #print(pid)
        self.val = validate(header)
        self.uid = self.val['data']['user_id']
        self.page = 1
        print(self.uid)
        self.res = getHglist(header, self.uid, self.page)
        print(self.res)
        self.res = self.res['data']
        print(self.res)
        self.long = len(self.res) / 4
        if len(self.res):
            #print(1111)
            self.id1.setText(str(self.res[(self.page - 1)]['id']))
            self.id2.setText(str(self.res[(self.page - 1) + 1]['id']))
            self.id3.setText(str(self.res[(self.page - 1) + 2]['id']))
            self.id4.setText(str(self.res[(self.page - 1) + 3]['id']))
            self.point1.setText(str(self.res[(self.page - 1)]['score']))
            self.point2.setText(str(self.res[(self.page - 1) + 1]['score']))
            self.point3.setText(str(self.res[(self.page - 1) + 2]['score']))
            self.point4.setText(str(self.res[(self.page - 1) + 3]['score']))
            self.card1.setText(self.res[0]['card'][0] + self.res[0]['card'][1] + self.res[0]['card'][2])
            self.card2.setText(self.res[1]['card'][0] + self.res[1]['card'][1] + self.res[1]['card'][2])
            self.card3.setText(self.res[2]['card'][0] + self.res[2]['card'][1] + self.res[2]['card'][2])
            self.card4.setText(self.res[3]['card'][0] + self.res[3]['card'][1] + self.res[3]['card'][2])

    def nextpage1(self):
        self.page += 1
        self.res = getHglist(header, self.uid, self.page)
        print(self.res)
        self.res = self.res['data']
        print(self.res)
        self.long = len(self.res) / 4
        if len(self.res):
            print(1111)
            print(str(self.res[(self.page - 1)]['id']))
            self.id1.setText(str(self.res[0]['id']))
            self.id2.setText(str(self.res[1]['id']))
            self.id3.setText(str(self.res[2]['id']))
            self.id4.setText(str(self.res[3]['id']))
            self.point1.setText(str(self.res[0]['score']))
            self.point2.setText(str(self.res[1]['score']))
            self.point3.setText(str(self.res[2]['score']))
            self.point4.setText(str(self.res[3]['score']))
            self.card1.setText(self.res[0]['card'][0]+self.res[0]['card'][1]+self.res[0]['card'][2])
            self.card2.setText(self.res[1]['card'][0]+self.res[1]['card'][1]+self.res[1]['card'][2])
            self.card3.setText(self.res[2]['card'][0]+self.res[2]['card'][1]+self.res[2]['card'][2])
            self.card4.setText(self.res[3]['card'][0]+self.res[3]['card'][1]+self.res[3]['card'][2])

    def frontpage1(self):
        if self.page > 1:
            self.page -= 1
            self.res = getHglist(header, self.uid, self.page)
            print(self.res)
            self.res = self.res['data']
            print(self.res)
            self.long = len(self.res) / 4
            if len(self.res):
                print(1111)
                self.id1.setText(str(self.res[(self.page - 1) * 4]['id']))
                self.id2.setText(str(self.res[(self.page - 1) * 4 + 1]['id']))
                self.id3.setText(str(self.res[(self.page - 1) * 4 + 2]['id']))
                self.id4.setText(str(self.res[(self.page - 1) * 4 + 3]['id']))
                self.point1.setText(str(self.res[(self.page - 1) * 4]['score']))
                self.point2.setText(str(self.res[(self.page - 1) * 4 + 1]['score']))
                self.point3.setText(str(self.res[(self.page - 1) * 4 + 2]['score']))
                self.card1.setText(self.res[(self.page - 1) * 4]['card'][0] + self.res[(self.page - 1) * 4]['card'][1] +
                                   self.res[(self.page - 1) * 4]['card'][2])
                self.card2.setText(
                    self.res[(self.page - 1) * 4 + 1]['card'][0] + self.res[(self.page - 1) * 4]['card'][1] +
                    self.res[(self.page - 1) * 4]['card'][2])
                self.card3.setText(
                    self.res[(self.page - 1) * 4 + 2]['card'][0] + self.res[(self.page - 1) * 4]['card'][1] +
                    self.res[(self.page - 1) * 4]['card'][2])
                self.card4.setText(
                    self.res[(self.page - 1) * 4 + 3]['card'][0] + self.res[(self.page - 1) * 4]['card'][1] +
                    self.res[(self.page - 1) * 4]['card'][2])
    def search(self):
        gid = self.lineEdit.text()
        if gid:
            response = getHgmore(header, gid)
            self.res = response['data']
            if response['status'] == 0:
                if len(self.res):
                    self.id1.setText(str(self.res['detail'][0]['name']))
                    self.id2.setText(str(self.res['detail'][1]['name']))
                    self.id3.setText(str(self.res['detail'][2]['name']))
                    self.id4.setText(str(self.res['detail'][3]['name']))
                    self.point1.setText(str(self.res['detail'][0]['score']))
                    self.point2.setText(str(self.res['detail'][1]['score']))
                    self.point3.setText(str(self.res['detail'][2]['score']))
                    self.point4.setText(str(self.res['detail'][3]['score']))
                    self.card1.setText(self.res['detail'][0]['card'][0]+self.res['detail'][0]['card'][1]+self.res['detail'][0]['card'][2])
                    self.card2.setText(self.res['detail'][1]['card'][0]+self.res['detail'][1]['card'][1]+self.res['detail'][1]['card'][2])
                    self.card3.setText(self.res['detail'][2]['card'][0]+self.res['detail'][2]['card'][1]+self.res['detail'][2]['card'][2])
                    self.card4.setText(self.res['detail'][3]['card'][0]+self.res['detail'][3]['card'][1]+self.res['detail'][3]['card'][2])
    # 返回按钮
    def backmenu(self):
        self.close()
        menuPale = winmenu(window)
        menuPale.setFixedSize(1039, 757)
        #menuPale.resize(1039, 757)
        menuPale.show()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = Mywindow()
    #window.resize(1039, 757)
    window.setFixedSize(1099, 745)
    #window.pushButton.clicked.connect(b_login)
    window.show()

    sys.exit(app.exec_())
