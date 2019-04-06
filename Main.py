# -*- coding: utf-8 -*-

import threading

from PyQt5 import QtWidgets
from OpenGL.GLUT import *
from Gui import design
from Environment.Environment import *
import Utils as utils


class Apps(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.environment = Environment()  # Инициализирую среду
        path = "null"
        for i in range(len(sys.argv)):
            if i == "-o":
                if i + 1 < len(sys.argv):
                    path = sys.argv[i + 1]
        if path != "null":
            self.environment = pickle.load(path)
        else:
            self.environment.setup()  # Произвожу первоначальную настройку

        self.setupUi(self)  # Инициализирую gui
        t1 = threading.Thread(target=self.__update)
        t1.start()
        self.label_5.setText(str(len(self.environment.food)))

    def __update(self):
        while True:
            self.openGLWidget._upgrade(self.environment.bots, self.environment.food)
            self.environment.update()
            self.label_9.setText(str(self.environment.epoch))
            self.label_3.setText(str(len(self.environment.bots)))


def main():

    if len(sys.argv) > 1:
        path = "null"
        mode = "test"
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-o":
                if i + 1 < len(sys.argv):
                    path = sys.argv[i + 1]
            if sys.argv[i] == "-train":
                mode = "train"

        print(utils.bordered("Information", " Run the program with arguments: {0},\n Path: {1}, Mode: {2}".format(sys.argv, path,mode)))
        if mode == "train":
            environment = Environment()
            if path != "null":
                f = open(path, 'rb')
                environment = pickle.load(f)
                f.close()
            else:
                environment.setup()
            while True:
                environment.update()
        else:
            app = QtWidgets.QApplication(sys.argv)
            window = Apps()
            window.show()
            app.exec_()



if __name__ == '__main__':
    main()
