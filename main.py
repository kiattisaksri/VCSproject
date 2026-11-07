import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTimer ,QDateTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)
        timer = QTimer(self)
        #timer.timeout.connect(self.updateTime)
        #timer.start(1000)  # Update every second
        #self.updateTime()  # Initial call to display time immediately




if __name__ == '__main__':       
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())