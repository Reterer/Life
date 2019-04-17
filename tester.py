import sys
from IHMDrawDates import Ui_MplMainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import numpy as np
import datetime


class DesignerMainWindow(QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        # connect the signals with the slots
        self.buttonDrawDate.clicked.connect(self.drawDate)
        self.buttonErase.clicked.connect(self.eraseDate)
    def drawDate(self):
#        base = datetime.datetime(2018, 1, 1)
#        x = np.array([base + datetime.timedelta(hours=i) for i in range(24)])
#        y = np.random.rand(len(x))
        x = np.arange(0,100,0.1)
        y = np.sin(x)
        self.mpl.canvas.ax.plot(x,y)
        self.mpl.canvas.ax.relim()
        self.mpl.canvas.ax.autoscale(True)
        self.mpl.canvas.draw()
    def eraseDate(self):
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.draw()


if __name__ == '__main__':
    app=0
    app = QApplication(sys.argv)
    dmw = DesignerMainWindow()
    # show it
    dmw.show()
    sys.exit(app.exec_())