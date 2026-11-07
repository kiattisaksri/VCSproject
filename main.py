import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTimer ,QDateTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()




if __name__ == '__main__':       
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())