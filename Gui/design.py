# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QCheckBox, QPushButton

import Config as Config
from Gui.OpenGLWidget import GLWidget, MplWidgetTest


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(893, 624)

		self.main_widget = QtWidgets.QWidget(MainWindow)
		self.main_widget.setObjectName("main_widget")

		self.grid_layout = QtWidgets.QGridLayout(self.main_widget)
		self.grid_layout.setObjectName("grid_layout")

		self.splitter = QtWidgets.QSplitter(self.main_widget)
		self.splitter.setOrientation(QtCore.Qt.Horizontal)
		self.splitter.setObjectName("splitter")

		self.openGLWidget = GLWidget(self)
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

		self.label_dump = QtWidgets.QLabel(self.gbSettings)
		self.label_dump.setObjectName("label_dump")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_dump)

		self.label_dump_count = QtWidgets.QLabel(self.gbSettings)
		self.label_dump_count.setObjectName("label_dump")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_dump_count)

		self.label_epoch = QtWidgets.QLabel(self.gbSettings)
		self.label_epoch.setObjectName("label_epoch")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_epoch)

		self.label_epoch_count = QtWidgets.QLabel(self.gbSettings)
		self.label_epoch_count.setObjectName("label_epoch_count")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_epoch_count)

		self.label_bots = QtWidgets.QLabel(self.gbSettings)
		self.label_bots.setObjectName("label_bots")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_bots)

		self.label_bots_count = QtWidgets.QLabel(self.gbSettings)
		self.label_bots_count.setObjectName("label_bots_count")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_bots_count)

		self.label_food = QtWidgets.QLabel(self.gbSettings)
		self.label_food.setObjectName("label_food")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_food)

		self.label_food_count = QtWidgets.QLabel(self.gbSettings)
		self.label_food_count.setObjectName("label_food_count")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_food_count)

		# Тут чекбокс

		self.button_reload = QPushButton('Обновить', self.gbSettings)
		self.button_reload.setObjectName("button_1")
		self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.button_reload)

		self.check_box_auto_reload = QCheckBox(self.gbSettings)
		self.check_box_auto_reload.setObjectName("check_box_1")
		self.check_box_auto_reload.setChecked(True)
		self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.check_box_auto_reload)

		self.splitter_box = QtWidgets.QSplitter(self.gbSettings)
		self.splitter_box.setLineWidth(0)
		self.splitter_box.setOrientation(QtCore.Qt.Vertical)
		self.splitter_box.setObjectName("splitter_2")

		self.group_box_statistic = QtWidgets.QGroupBox(self.splitter_box)
		self.group_box_statistic.setMinimumSize(QtCore.QSize(0, 100))
		self.group_box_statistic.setTitle("")
		self.group_box_statistic.setFlat(True)
		self.group_box_statistic.setObjectName("group_box_statistic")

		self.gridLayout_2 = QtWidgets.QGridLayout(self.group_box_statistic)

		self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_2.setSpacing(0)
		self.gridLayout_2.setObjectName("gridLayout_2")

		self.splitter_2 = QtWidgets.QSplitter(self.group_box_statistic)
		self.splitter_2.setLineWidth(0)
		self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
		self.splitter_2.setObjectName("splitter_2")

		self.tab_box_scores = QtWidgets.QTableWidget(self.splitter_2)
		self.tab_box_scores.setMinimumSize(QtCore.QSize(0, 0))
		self.tab_box_scores.setLineWidth(0)
		self.tab_box_scores.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.tab_box_scores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tab_box_scores.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tab_box_scores.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tab_box_scores.setObjectName("tab_box_scores")
		self.tab_box_scores.horizontalHeader().setStretchLastSection(True)
		self.tab_box_scores.setColumnCount(3)
		self.tab_box_scores.setHorizontalHeaderLabels(["#", "Score", 'Eaten food'])
		self.tab_box_scores.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)

		self.tab_box_info = QtWidgets.QTableWidget(self.splitter_2)
		self.tab_box_info.horizontalHeader().setStretchLastSection(True)
		self.tab_box_info.setLineWidth(0)
		self.tab_box_info.setColumnCount(2)
		self.tab_box_info.setRowCount(5)
		self.tab_box_info.setItem(0, 0, QtWidgets.QTableWidgetItem("ID"))
		self.tab_box_info.setItem(1, 0, QtWidgets.QTableWidgetItem("X"))
		self.tab_box_info.setItem(2, 0, QtWidgets.QTableWidgetItem("Y"))
		self.tab_box_info.setItem(3, 0, QtWidgets.QTableWidgetItem("Energy"))
		self.tab_box_info.setItem(4, 0, QtWidgets.QTableWidgetItem("Eaten food:"))
		self.tab_box_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.tab_box_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tab_box_info.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tab_box_info.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tab_box_info.setObjectName("tab_box_info")
		self.tab_box_info.setHorizontalHeaderLabels(["Key", "Value"])
		self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

		header = self.tab_box_scores.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

		header = self.tab_box_info.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

		self.mpl = MplWidgetTest(self.splitter_box)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
		self.mpl.setSizePolicy(sizePolicy)
		self.mpl.setObjectName("mpl")

		self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.splitter_box)

		self.grid_layout.addWidget(self.splitter, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.main_widget)
		self.translateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def translateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle("Live")
		self.gbSettings.setTitle("Settings")
		self.label_dump.setText("Dump:")
		self.label_dump_count.setText("Null")
		self.label_epoch.setText("Epoch:")
		self.label_epoch_count.setText("0")
		self.label_bots.setText("Bots:")
		self.label_bots_count.setText("0")
		self.label_food.setText("Food:                    ")
		self.label_food_count.setText("0")
		self.tab_box_scores.setSortingEnabled(True)
		self.tab_box_scores.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
