import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        button = QPushButton ("Press me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Click")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()