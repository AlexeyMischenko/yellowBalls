import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPolygonF
from PyQt5 import uic
from random import randint


class Balls(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.do_paint = False
        self.qp = QPainter()

    def draw(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            q = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(200, 200, q, q)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Balls()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
