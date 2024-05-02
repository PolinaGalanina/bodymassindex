from PyQt5.QtWidgets import *

from instr import *


class FinalWin(QWidget):
    def __init__(self, height, weight):
        super().__init__()
        self.index = self.calc_index(p1, p2, p3)
        self.health = self.calc_health(age, self.index)
        self.set_appear()
        self.set_ui()

    def calc_health(self, height, weight , index):
        if self.index < 20 : return "недовес"
        if  20 < self.index < 25 : return "норма"
        if 26 < self.index < 30 : return "избыточный вес"
        if 31 < self.index < 50 : return "ожирение"
        

    def calc_index(self,height, weight):
        return (weight/(height*height))


    def set_ui(self):
        index = QLabel('Ваш ИМТ : ' + str(self.index))
        
        line = QVBoxLayout()
        line.addWidget(index)
        

        self.setLayout(line)