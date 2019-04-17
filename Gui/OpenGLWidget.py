# -*- coding: utf-8 -*-

from OpenGL import GL, GLU
from PyQt5.QtCore import QPoint, QRect, Qt
from PyQt5.QtGui import (QBrush, QColor, QFont, QPainter, QPen)
from PyQt5.QtWidgets import QOpenGLWidget, QSizePolicy, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import Config as Config
import Utils as utils
import matplotlib.pyplot as plt


class Helper(object):

    def __init__(self, *args):

        self.background = QBrush(QColor(0, 0, 0))
        self.circlePen = QPen(Qt.black)
        self.circlePen.setWidth(1)

        self.textPen = QPen(Qt.white)
        self.textFont = QFont()
        self.textFont.setPixelSize(Config.FONT_SIZE)
        self.env = args[0]

    def paint(self, painter, event):
        try:
            painter.fillRect(event.rect(), self.background)  # Очищаем и красим фон

            for i in range(len(self.env.bots)):
                painter.setBrush(
                    QBrush(QColor(self.env.bots[i].color[0], self.env.bots[i].color[1], self.env.bots[i].color[2])))
                painter.setPen(self.circlePen)
                painter.drawEllipse(QRect(self.env.bots[i].x + self.env.bots[i].radius / 2,
                                          self.env.bots[i].y + self.env.bots[i].radius / 2,
                                          self.env.bots[i].radius,
                                          self.env.bots[i].radius))
                painter.setPen(self.textPen)
                painter.setFont(self.textFont)
                painter.drawText(QPoint(self.env.bots[i].x, self.env.bots[i].y),
                                 str(self.env.bots[i].id) + " | " + str(round(self.env.bots[i].energy)))

            for i in range(len(self.env.food)):
                painter.setBrush(
                    QBrush(QColor(self.env.food[i].color[0], self.env.food[i].color[1], self.env.food[i].color[2])))
                painter.setPen(self.circlePen)
                painter.drawEllipse(self.env.food[i].x + self.env.food[i].radius / 2,
                                    self.env.food[i].y + self.env.food[i].radius / 2,
                                    self.env.food[i].radius, self.env.food[i].radius)

        except Exception as e:
            print(utils.bordered("Error-Draw", " Message: {0}".format(e)))


class GLWidget(QOpenGLWidget):

    def __init__(self, parent):
        super(GLWidget, self).__init__(parent.splitter)
        self.helper = Helper(parent.environment)
        self.setAutoFillBackground(True)

    def initializeGL(self):
        GL.glShadeModel(GL.GL_SMOOTH)
        GLU.gluOrtho2D(0, 0, 0, 0)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        self.helper.paint(painter, event)
        painter.end()


class MplCanvas(FigureCanvas):

    def __init__(self):
        plt.style.use(['dark_background'])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    def plot(self, data):

        ax = self.fig
        ax.patch.set_facecolor('#323232')
        xx = ax.add_subplot(111)
        xx.patch.set_facecolor('#323232')
        xx.plot(data, 'o-')
        xx.margins(y=.1)
        xx.set_title('')
        plt.grid(True)
        plt.ion()
        plt.draw()


class MplWidgetTest(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.ntb = NavigationToolbar(self.canvas, self)
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.ntb)
        self.setLayout(self.vbl)
