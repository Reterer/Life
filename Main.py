# -*- coding: utf-8 -*-

from OpenGL import GL
from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex2f
from PyQt5 import QtWidgets
from OpenGL.GLUT import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QTableWidgetItem
from Gui import design
import math
from Environment.Environment import *


class Apps(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.environment = Environment()                                            # Инициализирую среду
        self.environment.setup()                                                    # Произвожу первоначальную настройку
        self.setupUi(self)                                                          # Инициализирую gui
        self.openGLWidget.paintGL = self.paintGL                                    # Фунция отрисовки

        timer = QTimer(self)                                                        # Инициализирую таймер
        timer.timeout.connect(self.__update)
        timer.start(1)                                                              # Запускаю таймер

    def __update(self):                                                             # Функция обновления
        self.environment.update()                                                   # Обновление среды
        if self.checkBox.isChecked():
            self.openGLWidget.update()                                              # Обновление кадра
        if self.checkBox_2.isChecked():                                             # Обновляю статистику
            self.tbScores.setRowCount(len(self.environment.bots))
            for i in range(len(self.environment.bots)):
                self.tbScores.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tbScores.setItem(i, 1, QTableWidgetItem(str(self.environment.bots[i].energy)))
            self.tbScores.setColumnWidth(0, 20)
            self.label_3.setText(str(len(self.environment.bots)))
            self.label_5.setText(str(len(self.environment.food)))

    def paintGL(self):                                                              # Функция отрисовки
        # Очищаю экран #
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glPushMatrix()
        GL.glEnable(0x809D)
        GL.glTranslatef(-0.25, -0.10, 0.0)
        GL.glScalef(0.75, 1.15, 0.0)
        GL.glRotatef(0.0, 0.0, 0.0, 1.0)
        GL.glPopMatrix()

        # Русую ботов #
        for i in range(len(self.environment.bots)):
            if self.environment.bots[i].radius >= 2:
                GL.glColor3f(self.environment.bots[i].color[0], self.environment.bots[i].color[1],
                             self.environment.bots[i].color[2])
                GL.glBegin(GL.GL_POLYGON)
                for angle in range(0, 360, 30):
                    glVertex2f(
                        self.environment.bots[i].radius * math.cos(angle * 3.142 / 180) + self.environment.bots[i].x,
                        self.environment.bots[i].radius * math.sin(angle * 3.142 / 180) + self.environment.bots[i].y)
                GL.glEnd()

        # Русую еду #
        for i in range(len(self.environment.food)):
            if self.environment.food[i].radius >= 2:
                GL.glColor3f(self.environment.food[i].color[0], self.environment.food[i].color[1],
                             self.environment.food[i].color[2])
                GL.glBegin(GL.GL_POLYGON)
                for angle in range(0, 360, 30):
                    glVertex2f(
                        self.environment.food[i].radius * math.cos(angle * 3.142 / 180) + self.environment.food[i].x,
                        self.environment.food[i].radius * math.sin(angle * 3.142 / 180) + self.environment.food[i].y)
                GL.glEnd()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Apps()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
