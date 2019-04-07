# -*- coding: utf-8 -*-

from OpenGL import GL, GLU
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import (QBrush, QColor, QFont, QPainter, QPen)
from PyQt5.QtWidgets import QOpenGLWidget

import Config as Config
import Utils as utils


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
            painter.fillRect(event.rect(), self.background)
            painter.save()
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
            painter.restore()
        except Exception as e:
            print(utils.bordered("Error-Draw", " Message: {0}".format(e)))


class GLWidget(QOpenGLWidget):

    def __init__(self, helper, parent):
        super(GLWidget, self).__init__(parent.splitter)
        self.helper = helper
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
