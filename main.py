import login1
import menu

from PyQt5.Qt import *
import sys
if __name__ == '__main__':

    app = QApplication(sys.argv)

    login = login1.Ui_Dialog()

    login.show()
