import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox, QPlainTextEdit,QHBoxLayout)

from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1=QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1=QPushButton("Message", self)
        self.btn1.clicked.connect(self.activateMessage)
        
        self.btn2=QPushButton("clear", self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout()  # 수평 박스 레이아웃 생성
        hbox.addStretch(1)  # 공백 추가
        hbox.addWidget(self.btn1)  # 버튼 추가
        hbox.addWidget(self.btn2)  # 버튼 추가

        vbox = QVBoxLayout()  # 수직 박스 레이아웃 생성
        vbox.addWidget(self.te1)  # 텍스트 입력창 추가

        vbox.addLayout(hbox)  
        vbox.addStretch(1)  # 빈 공간 추가

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')  # 창 제목 설정
        self.setWindowIcon(QIcon('icon.png'))  # 윈도우 아이콘 설정
        self.resize(256, 256)  # 창 크기 설정
        self.show()

    def activateMessage(self):
        """ 버튼 클릭 시 메시지 박스 표시 """
        QMessageBox.information(self, "Information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        """ 텍스트 필드 초기화 """
        self.te1.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
