# bodymassindex

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget,QCheckBox
from PyQt5.QtGui import QPixmap, QIcon

class First(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('books.png'))

        line = QVBoxLayout()

        pic_label = QLabel()
        picture = QPixmap('cat.jpg')
        pic_label.setPixmap(picture)
        line.addWidget(pic_label)

        answer_list = QListWidget()
        answer_list.addItems(['1','2','три'])

        line.addWidget(answer_list)

        btn1 = QCheckBox('пункт1')
        btn2 = QCheckBox('пункт2')
        line.addWidget(btn1)
        line.addWidget(btn2)

        self.setLayout(line)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    win1 = First()
    app.exec()