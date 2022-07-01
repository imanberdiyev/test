from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit 
from instr import*


class FinalWin(QWidget):
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
        self.index=QLabel(txt_index)
        self.txt_workheart=QLabel(txt_workheart)
        self.m_line=QVBoxLayout()
        self.m_line.addWidget(self.index, alignment = Qt.AlignCenter)
        self.m_line.addWidget(self.txt_workheart, alignment =Qt.AlignCenter)
        self.setLayout(self.m_line)

    def connects(self):
        pass
        
    def next_click(self):
        pass
