# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from OpenGL import GL, GLU
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import (QBrush, QColor, QFont, QLinearGradient, QPainter, QPen)
from PyQt5.QtWidgets import QOpenGLWidget
import Config as Config


class Helper(object):

    def __init__(self):
        gradient = QLinearGradient(QPointF(50, -20), QPointF(80, 20))
        gradient.setColorAt(0.0, Qt.white)
        gradient.setColorAt(1.0, QColor(0xa6, 0xce, 0x39))

        self.background = QBrush(QColor(0, 0, 0))
        self.circleBrush = QBrush(QColor(255, 0, 0))
        self.food = QBrush(QColor(0, 255, 0))
        self.circlePen = QPen(Qt.black)
        self.circlePen.setWidth(1)
        self.textPen = QPen(Qt.white)
        self.textFont = QFont()
        self.textFont.setPixelSize(50)

    def paint(self, painter, event, *args):
        painter.fillRect(event.rect(), self.background)
        painter.translate(100, 100)

        painter.save()
        painter.setBrush(self.circleBrush)
        painter.setPen(self.circlePen)

        for i in range(len(args[0])):
            painter.drawEllipse(args[0][i].x, args[0][i].y, args[0][i].radius, args[0][i].radius)

        painter.setBrush(self.food)
        for i in range(len(args[1])):
            painter.drawEllipse(args[1][i].x, args[1][i].y, args[1][i].radius, args[1][i].radius)

        painter.restore()
        painter.setPen(self.textPen)
        painter.setFont(self.textFont)


class GLWidget(QOpenGLWidget):

    def __init__(self, helper, parent):
        super(GLWidget, self).__init__(parent.splitter)
        self.this = parent
        self.helper = helper
        self.elapsed = 0
        self.setAutoFillBackground(False)
        self.bots = []
        self.food = []

    def initializeGL(self):
        GL.glClearColor(0, 0, 0, 0)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GLU.gluOrtho2D(0, Config.HEIGHT_MAP, 0, Config.WIDTH_MAP)

    def _upgrade(self, *args):
        self.bots = args[0]
        self.food = args[1]
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.bots, self.food)
        painter.end()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        helper = Helper()
        self.openGLWidget = GLWidget(helper, self)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, Config.HEIGHT_MAP, Config.WIDTH_MAP))
        self.openGLWidget.setMinimumSize(Config.HEIGHT_MAP, Config.WIDTH_MAP)
        self.openGLWidget.setObjectName("openGLWidget")

        self.gbSettings = QtWidgets.QGroupBox(self.splitter)
        self.gbSettings.setMinimumSize(QtCore.QSize(215, 0))
        self.gbSettings.setObjectName("gbSettings")

        self.formLayout = QtWidgets.QFormLayout(self.gbSettings)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(10, 5, 5, 39)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setObjectName("formLayout")
        self.labelUpdate = QtWidgets.QLabel(self.gbSettings)
        self.labelUpdate.setObjectName("labelUpdate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUpdate)
        self.spinBox = QtWidgets.QSpinBox(self.gbSettings)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.labelDump = QtWidgets.QLabel(self.gbSettings)
        self.labelDump.setObjectName("labelDump")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDump)
        self.label_7 = QtWidgets.QLabel(self.gbSettings)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.gbSettings)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.gbSettings)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.labelBots = QtWidgets.QLabel(self.gbSettings)
        self.labelBots.setObjectName("labelBots")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelBots)
        self.label_3 = QtWidgets.QLabel(self.gbSettings)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.labelFood = QtWidgets.QLabel(self.gbSettings)
        self.labelFood.setObjectName("labelFood")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelFood)
        self.label_5 = QtWidgets.QLabel(self.gbSettings)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.labelDraw = QtWidgets.QLabel(self.gbSettings)
        self.labelDraw.setObjectName("labelDraw")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelDraw)
        self.checkBox = QtWidgets.QCheckBox(self.gbSettings)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.gbStatistic = QtWidgets.QGroupBox(self.gbSettings)
        self.gbStatistic.setMinimumSize(QtCore.QSize(0, 100))
        self.gbStatistic.setTitle("")
        self.gbStatistic.setFlat(False)
        self.gbStatistic.setObjectName("gbStatistic")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gbStatistic)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.gbStatistic)
        self.splitter_2.setLineWidth(0)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tbScores = QtWidgets.QTableWidget(self.splitter_2)
        self.tbScores.setMinimumSize(QtCore.QSize(0, 0))
        self.tbScores.setLineWidth(0)
        self.tbScores.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbScores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbScores.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbScores.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbScores.setObjectName("tbScores")
        self.tbScores.horizontalHeader().setStretchLastSection(True)
        self.tbScores.setColumnCount(2)
        self.tbScores.setHorizontalHeaderLabels(["#", "Счёт"])
        self.tbScores.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tbInfo = QtWidgets.QTableWidget(self.splitter_2)
        self.tbInfo.horizontalHeader().setStretchLastSection(True)
        self.tbInfo.setLineWidth(0)
        self.tbInfo.setColumnCount(2)
        self.tbInfo.setHorizontalHeaderLabels(["Ключ", "Значение"])
        self.tbInfo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbInfo.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tbInfo.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbInfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbInfo.setObjectName("tbInfo")
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.gbStatistic)
        self.gbRun = QtWidgets.QGroupBox(self.gbSettings)
        self.gbRun.setTitle("")
        self.gbRun.setAlignment(QtCore.Qt.AlignCenter)
        self.gbRun.setFlat(False)
        self.gbRun.setCheckable(False)
        self.gbRun.setObjectName("gbRun")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbRun)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ibCommand = QtWidgets.QLineEdit(self.gbRun)
        self.ibCommand.setInputMask("")
        self.ibCommand.setObjectName("ibCommand")
        self.gridLayout_3.addWidget(self.ibCommand, 0, 0, 1, 1)
        self.btnRun = QtWidgets.QToolButton(self.gbRun)
        self.btnRun.setObjectName("btnRun")
        self.gridLayout_3.addWidget(self.btnRun, 0, 1, 1, 1)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.gbRun)
        self.label = QtWidgets.QLabel(self.gbSettings)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gbSettings)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBox_2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.gbSettings.setTitle(_translate("MainWindow", "Настройки"))
        self.labelUpdate.setText(_translate("MainWindow", "Update Timer"))
        self.labelDump.setText(_translate("MainWindow", "Dump: "))
        self.label_7.setText(_translate("MainWindow", "Null"))
        self.label_8.setText(_translate("MainWindow", "Epoh:"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.labelBots.setText(_translate("MainWindow", "Bots:"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.labelFood.setText(_translate("MainWindow", "Food:                    "))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.labelDraw.setText(_translate("MainWindow", "Draw:"))
        self.checkBox.setText(_translate("MainWindow", "(Y/N)"))
        self.btnRun.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Update: "))
        self.checkBox_2.setText(_translate("MainWindow", "(Y/N)"))
        self.tbScores.setSortingEnabled(True)
        self.tbScores.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
