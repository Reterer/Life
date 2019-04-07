# -*- coding: utf-8 -*-

from threading import Thread

import qdarkgraystyle
from OpenGL.GLUT import *
from PyQt5 import QtWidgets
from Environment.Environment import *
from Gui import design


class Apps(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self, path):
        super().__init__()
        self.environment = Environment()  # Инициализирую среду

        if path != "null":
            f = open(path, 'rb')
            self.environment = pickle.load(f)
            print(utils.bordered("Information",
                                 " Bots: {0}, Epoch: {1}".format(len(self.environment.bots), self.environment.epoch)))
            f.close()
        else:
            self.environment.setup()  # Произвожу первоначальную настройку
            print(utils.bordered("Information",
                                 " Data: {0},\n Epoch: {1}, Bots: {2}".format(
                                     datetime.datetime.today().strftime("%m-%d-%Y %H-%M-%S"), 0,
                                     len(self.environment.bots))))

        self.setupUi(self)  # Инициализирую gui

        thread = Thread(target=self.__update, args=())
        thread.daemon = True
        thread.start()

        self.label_5.setText(str(len(self.environment.food)))
        self.label_7.setText(path)

    def __update(self):
        i = 0
        while True:
            try:
                self.environment.update()   # Обновляем среду
                if i == 3:
                    self.openGLWidget.update()   # Обновляем экран
                    time.sleep(0.001)
                    i = 0

                i += 1
                self.label_9.setText(str(self.environment.epoch))   # Обновляем кол-во эпох
                self.label_3.setText(str(len(self.environment.bots)))   # Обновляем кол-во ботов
            except Exception as e:
                print(utils.bordered("Error", "Message: {0}".format(e)))
                traceback.print_exc()


def main():
    if len(sys.argv) > 0:
        path = "null"
        mode = "test"
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-o":
                if i + 1 < len(sys.argv):
                    path = sys.argv[i + 1]
            if sys.argv[i] == "-train":
                mode = "train"

        print(utils.bordered("Information",
                             " Run the program with arguments: {0},\n Path: {1}, Mode: {2}".format(sys.argv, path,
                                                                                                   mode)))
        if mode == "train":
            environment = Environment()
            if path != "null":
                f = open(path, 'rb')
                environment = pickle.load(f)
                print(utils.bordered("Information",
                                     " Bots: {0}, Epoch: {1}".format(len(environment.bots), environment.epoch)))
                f.close()
            else:
                environment.setup()
                print(utils.bordered("Information",
                                     " Data: {0},\n Epoch: {1}, Bots: {2}".format(
                                         datetime.datetime.today().strftime("%m-%d-%Y %H-%M-%S"), 0,
                                         len(environment.bots))))

            while True:
                environment.update()
        else:
            app = QtWidgets.QApplication(sys.argv)
            app.setStyleSheet(qdarkgraystyle.load_stylesheet())
            window = Apps(path)
            window.show()
            app.exec_()


if __name__ == '__main__':
    main()
