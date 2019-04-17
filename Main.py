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
		self.auto_reload = 10

		if path != "null" and os.path.isfile(path):

			f = open(path, 'rb')
			self.environment = pickle.load(f)
			print(utils.bordered("Information",
								 " Bots: {0}, Epoch: {1}".format(len(self.environment.bots), self.environment.epoch)))
			f.close()
		else:
			self.environment.setup()  # Произвожу первоначальную настройку
			print(utils.bordered("Information",
								 " Data: {0} \n Epoch: {1}, Bots: {2}".format(
									 datetime.datetime.today().strftime("%m-%d-%Y %H-%M-%S"), 0,
									 len(self.environment.bots))))

		self.setupUi(self)  # Инициализирую gui

		thread = Thread(target=self.__update, args=())
		thread.daemon = True
		thread.start()

		self.label_food_count.setText(str(len(self.environment.food)))
		self.label_dump_count.setText(path)
		self.button_reload.clicked.connect(self.__update_tabs)
		self.tab_box_scores.doubleClicked.connect(self.doubleClicked_table)
		self.mpl.canvas.plot(self.environment.history)
		self.check_box_auto_reload.setText("Auto-update {0}s.".format(self.auto_reload))

	def __update(self):
		self.last_save = time.time()

		counter = 0
		while True:
			try:
				if self.environment.crt_iter == self.environment.iter_for_epoch - 1:
					j = 0
					for i in self.environment.bots:
						j += i.eat_food
					self.environment.history.append(j)
					self.mpl.canvas.plot(self.environment.history)
				if self.last_save + self.auto_reload < time.time():
					if self.check_box_auto_reload.isChecked():
						self.__update_tabs()
						self.last_save = time.time()
				self.environment.update()
				self.label_epoch_count.setText(str(self.environment.epoch))  # Обновляем кол-во эпох
				self.label_bots_count.setText(str(len(self.environment.bots)))  # Обновляем кол-во ботов

				if counter == 1:
					self.openGLWidget.update()  # Обновляем экран
					time.sleep(0.001)
					counter = 0
				counter += 1
			except Exception as e:
				print(utils.bordered("Error", "Message: {0}".format(e)))
				traceback.print_exc()

	def doubleClicked_table(self):
		index = int(self.tab_box_scores.item(self.tab_box_scores.currentItem().row(), 0).text())

		found = False
		for i in self.environment.bots:
			if i.id == index:
				self.tab_box_info.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.id)))
				self.tab_box_info.setItem(1, 1, QtWidgets.QTableWidgetItem(str(i.x)))
				self.tab_box_info.setItem(2, 1, QtWidgets.QTableWidgetItem(str(i.y)))
				self.tab_box_info.setItem(3, 1, QtWidgets.QTableWidgetItem(str(i.energy)))
				self.tab_box_info.setItem(4, 1, QtWidgets.QTableWidgetItem(str(i.eat_food)))
				self.tab_box_info.setHorizontalHeaderLabels(["Key", "Value"])
				found = True

		if not found:
			self.__update_tabs()

	def __update_tabs(self):
		self.tab_box_scores.setRowCount(len(self.environment.bots))
		for c, i in enumerate(self.environment.bots):
			self.tab_box_scores.setItem(c, 0, QtWidgets.QTableWidgetItem(str(i.id)))
			self.tab_box_scores.setItem(c, 1, QtWidgets.QTableWidgetItem(str(int(i.energy))))
			self.tab_box_scores.setItem(c, 2, QtWidgets.QTableWidgetItem(str(int(i.eat_food))))
		self.tab_box_scores.setHorizontalHeaderLabels(["#", "Score", 'Eaten food'])


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
							 " Run the program with arguments: {0} \n Path: {1}, Mode: {2}".format(sys.argv, path,
																								   mode)))

		if mode == "train":
			environment = Environment()
			if path != "null" and os.path.isfile(path):
				f = open(path, 'rb')
				environment = pickle.load(f)
				print(utils.bordered("Information",
									 " Bots: {0}, Epoch: {1}".format(len(environment.bots), environment.epoch)))
				f.close()
			else:
				environment.setup()
				print(utils.bordered("Information",
									 " Data: {0} \n Epoch: {1}, Bots: {2}".format(
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
