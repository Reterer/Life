from OpenGL import GL
from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex2f
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from OpenGL.GLUT import *
from Gui import design
import math
from Environment.Environment import *


class Apps(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.environment = Environment()
        self.environment.setup()
        self.setupUi(self)
        self.openGLWidget.bots = self.environment.bots

        #self.scores.setRowCount(len(self.environment.bots))
        #self.scores.setHorizontalHeaderLabels(["#", "Счёт"])
        #for i in range(len(self.environment.bots)):
        #    self.scores.setItem(i, 0, QTableWidgetItem(str(self.environment.bots[i].id)))
        #    self.scores.setItem(i, 1, QTableWidgetItem(str(self.environment.bots[i].energy)))
        self.openGLWidget.paintGL = self.paintGL

    def paintGL(self):

        self.environment.update()
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glPushMatrix()
        GL.glEnable(0x809D)
        GL.glTranslatef(-0.25, -0.10, 0.0)
        GL.glScalef(0.75, 1.15, 0.0)
        GL.glRotatef(0.0, 0.0, 0.0, 1.0)
        GL.glPopMatrix()

        for i in range(len(self.environment.bots)):
            GL.glColor3f(self.environment.bots[i].color[0], self.environment.bots[i].color[1], self.environment.bots[i].color[2])
            GL.glBegin(GL.GL_POLYGON)
            for angle in range(0, 360, 30):
                glVertex2f(self.environment.bots[i].radius * math.cos(angle * 3.142 / 180) + self.environment.bots[i].x,
                           self.environment.bots[i].radius * math.sin(angle * 3.142 / 180) + self.environment.bots[i].y)
            GL.glEnd()
            #self.scores.setItem(i, 1, QTableWidgetItem(str(self.environment.bots[i].energy)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Apps()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
