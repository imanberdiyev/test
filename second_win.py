from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QVBoxLayout, QLineEdit 
from instr import*
from second_win import*

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.name=QLabel(txt_name)
        self.name_editor=QLineEdit()

        self.age=QLabel(txt_age)
        self.age_editor+QLineEdit 
        self.timer_txt=QLabel('00:00:00')
        self
    def connects(self):
        pass
        
    
    def next_click(self):
        pass

       
