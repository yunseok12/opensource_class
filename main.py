# 애플리케이션에 필요한 라이브러리 추가
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 애플리케이션 화면을 띄우기 위한 GUI 위젯
class Calculator(QWidget):  
    # QWidget 클래스를 상속받아서 클래스를 정의

    def __init__(self):
        super().__init__()  
        # 부모 클래스 QWidget을 초기화
        
        self.initUI()  
        # 나머지 초기화는 initUI 함수에서 정의

    def initUI(self):
        self.setWindowTitle('Calculator')  
        # 윈도우에 표시되는 타이틀
        self.resize(256, 256)  
        self.show()  
        # 윈도우 화면 표시

if __name__ == '__main__':  
    # PyQt는 애플리케이션 당 1개의 QApplication이 필요함
    app = QApplication(sys.argv)  
    # QApplication 인스턴스 생성
    view = Calculator()  
    # Calculator 윈도우 인스턴스 생성
    sys.exit(app.exec_())  
    # Application의 event 처리를 하도록 루프 생성
