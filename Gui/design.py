# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtOpenGL import QGL, QGLFormat, QGLWidget
from OpenGL import GL, GLU
import Config


class GLWidget(QGLWidget):

    def __init__(self, parent):
        super(GLWidget, self).__init__(QGLFormat(QGL.SampleBuffers), parent)
        self.startTimer(10)

    def initializeGL(self):
        GL.glClearColor(0, 0, 0, 0)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GLU.gluOrtho2D(0, Config.HEIGHT_MAP, 0, Config.WIDTH_MAP)

    def resizeGL(self, w, h):
        GL.glViewport(0, 0, Config.HEIGHT_MAP, Config.WIDTH_MAP)
        #GL.glViewport(0, 0, w, h)

    def timerEvent(self, event):
        self.update()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.openGLWidget = GLWidget(self.splitter)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, Config.HEIGHT_MAP, Config.WIDTH_MAP))
        self.openGLWidget.setMinimumSize(Config.HEIGHT_MAP, Config.WIDTH_MAP)
        self.openGLWidget.setObjectName("env")

        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(218, 541))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(10, 10, 5, 0)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.label_fps = QtWidgets.QLabel(self.groupBox)
        self.label_fps.setObjectName("label_fps")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_fps)
        self.fps = QtWidgets.QSpinBox(self.groupBox)
        self.fps.setMinimum(0)
        self.fps.setMaximum(100000)
        self.fps.setObjectName("fps")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fps)
        self.label_epoch = QtWidgets.QLabel(self.groupBox)
        self.label_epoch.setObjectName("label_epoch")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_epoch)
        self.label_epoch_count = QtWidgets.QLabel(self.groupBox)
        self.label_epoch_count.setObjectName("label_epoch_count")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_epoch_count)
        self.label_dump = QtWidgets.QLabel(self.groupBox)
        self.label_dump.setObjectName("label_dump")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_dump)
        self.label_pach_dump = QtWidgets.QLabel(self.groupBox)
        self.label_pach_dump.setObjectName("label_pach_dump")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_pach_dump)
        self.label_bot_visible = QtWidgets.QLabel(self.groupBox)
        self.label_bot_visible.setObjectName("label_bot_visible")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_bot_visible)
        self.checkBox_visible = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_visible.setText("")
        self.checkBox_visible.setObjectName("checkBox_visible")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox_visible)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line)

        self.scores = QtWidgets.QTreeView(self.groupBox)
        self.scores.setMinimumSize(QtCore.QSize(0, 250))
        self.scores.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scores.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.scores.setTabKeyNavigation(False)
        self.scores.setProperty("showDropIndicator", False)
        self.scores.setDragDropOverwriteMode(False)
        self.scores.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.scores.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.scores.setWordWrap(False)
        self.scores.setObjectName("scores")
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['#', 'Статистика'])
        self.scores.header().setDefaultSectionSize(20)
        self.scores.setModel(self.model)

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.scores)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройки"))
        self.label_fps.setText(_translate("MainWindow", "FPS:"))
        self.label_epoch.setText(_translate("MainWindow", "Epoch:"))
        self.label_epoch_count.setText(_translate("MainWindow", "0"))
        self.label_dump.setText(_translate("MainWindow", "Dump:"))
        self.label_pach_dump.setText(_translate("MainWindow", "NULL"))
        self.label_bot_visible.setText(_translate("MainWindow", "Bot Visible other:"))
        self.scores.setSortingEnabled(True)
        self.action.setText(_translate("MainWindow", "Новый"))
        self.action_2.setText(_translate("MainWindow", "Открыть"))
        self.action_3.setText(_translate("MainWindow", "Настройка среды"))
        self.action_5.setText(_translate("MainWindow", "Выйти"))
