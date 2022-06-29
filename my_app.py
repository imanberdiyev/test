from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QVBoxLayout, QLineEdit 
from instr import*
from second_win import*

class MainWin(QWidget):
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
        self.hello_txt=QLabel(txt_hello)
        self.intsruction=QLabel(txt_instruction)
        self.button=QPushButton(txt_next)

        self.Vlayout=QVBoxLayout()
        '''добавление в вертикальное расположение виджетов'''
        self.Vlayout.addWidget(self.hello_txt)
        self.Vlayout.addWidget(self.intsruction)
        self.Vlayout.addWidget(self.button)

        self.setLayout(self.Vlayout)


    def connects(self):
        self.button.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw=TestWin()
   
        
app=QApplication([])
main_win=MainWin()
app.exec_()
