import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QPoint, Qt


class Programm(QWidget):
    def __init__(self):
        # Конструктор QMainWindow
        super().__init__()

        # Загружаем UI
        uic.loadUi("Ui.ui", self)
        self.circles = []

        self.initUI()

    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)

        for circle in self.circles:
            painter.setBrush(QBrush(QColor(236, 255, 0)))
            painter.drawEllipse(QPoint(circle["x"], circle["y"]),
                                circle["r"], circle["r"])
        painter.end()

    def initUI(self):
        self.button_add.clicked.connect(self.create_new_ball)

    def create_new_ball(self):
        x, y = randint(0, self.width()), randint(0, self.height())  # позиция
        r = randint(20, 55)  # радиус
        # Добавляем круг
        self.circles.append({
            "x": x,
            "y": y,
            "r": r
        })
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec_())
