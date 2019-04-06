# -*- coding: utf-8 -*-

import threading

from PyQt5 import QtWidgets
from OpenGL.GLUT import *
from Gui import design
from Environment.Environment import *


class Apps(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.environment = Environment()  # Инициализирую среду
        self.environment.setup()  # Произвожу первоначальную настройку
        self.setupUi(self)  # Инициализирую gui
        t1 = threading.Thread(target=self.__update)
        t1.start()

    def __update(self):
        i = 0
        while True:

            if i == 1:
                self.openGLWidget._upgrade(self.environment.bots, self.environment.food)
                i = 0
            self.environment.update()
            i += 1


def main():
    print(sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[1] == "-train":
            environment = Environment()
            environment.setup()
            while True:
                environment.update()
        if sys.argv[1] == "-test":
            app = QtWidgets.QApplication(sys.argv)
            window = Apps()
            window.show()
            app.exec_()
    else:
        print("321")

if __name__ == '__main__':
    main()
