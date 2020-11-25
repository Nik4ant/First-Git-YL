import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from Ui import Ui_Form
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QPoint, Qt


class Programm(QWidget, Ui_Form):
    def __init__(self):
        # Конструктор QWidget
        super().__init__()

        # Загружаем UI
        self.setupUi(self)
        self.circles = []

        self.initUI()

    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)

        for circle in self.circles:
            painter.setBrush(QBrush(QColor(*circle["color"])))
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
            "r": r,
            "color": [randint(0, 255), randint(0, 255), randint(0, 255)]
        })
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Programm()
    ex.show()
    sys.exit(app.exec_())
