import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor


class Programm(QWidget):
    def __init__(self):
        # Конструктор QMainWindow
        super().__init__()

        # Загружаем UI
        uic.loadUi("Ui.ui", self)
        self.is_paint = False

        self.initUI()

    def initUI(self):
        self.button_add.clicked.connect(self.create_new_ball)

    def paintEvent(self, event):
        if self.is_paint:
            painter = QPainter(self)
            pen = QPen()
            pen.setColor(QColor("yellow"))

            painter.setPen(pen)
            painter.begin()
            x, y = randint(15, self.width() - 15), randint(15, self.width() - 15)
            r = randint(40, 150)
            painter.drawEllipse(x, y, r, r)
            self.is_paint = False
            painter.end()

    def create_new_ball(self):
        self.is_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec_())
