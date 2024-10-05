import sys
from PyQt6.QtWidgets import QApplication,QWidget ,QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

app=QApplication(sys.argv)
class miventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi ventana")
        self.button = QPushButton("mi boton")
        self.setCentralWidget(self.button)

ventana = miventana()
ventana.show()

app.exec()