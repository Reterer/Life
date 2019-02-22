from OpenGL import GL
from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex2f
from PyQt5 import QtWidgets
from OpenGL.GLUT import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Gui import design
import math
from Environment.Environment import *


class Apps(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.environment = Environment()
        self.environment.setup()
        self.setupUi(self)
        self.openGLWidget.paintGL = self.paintGL
        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()
        for i in range(len(self.environment.bots)):
            branch1 = QStandardItem(str(self.environment.bots[i].id))
            branch1.appendRow([QStandardItem("2"), QStandardItem("5")])
            branch1.appendRow([QStandardItem("3"), QStandardItem("6")])
            self.rootNode.appendRow([branch1, None])
        self.scores.setModel(self.model)
        self.scores.setAlternatingRowColors(True)

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

        for i in range(len(self.environment.food)):
            GL.glColor3f(self.environment.food[i].color[0], self.environment.food[i].color[1], self.environment.food[i].color[2])
            GL.glBegin(GL.GL_POLYGON)
            for angle in range(0, 360, 30):
                glVertex2f(self.environment.food[i].radius * math.cos(angle * 3.142 / 180) + self.environment.food[i].x,
                           self.environment.food[i].radius * math.sin(angle * 3.142 / 180) + self.environment.food[i].y)
            GL.glEnd()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Apps()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
