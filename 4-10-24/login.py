import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QGridLayout, QLabel

class login(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Log-In")
        self.setGeometry(600,100,300,300)

        layout = QGridLayout()
        self.user = QLineEdit()
        self.user.setPlaceholderText("Introduce tu usuario")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Introduce tu contraseña")
        boton = QPushButton("Iniciar Sesion")

        label1 = QLabel()
        label1.setText("Usuario")
        font = label1.font()
        font.setPointSize(30)

        label2 = QLabel()
        label2.setText("Contraseña")
        font = label2.font()
        font.setPointSize(30)

        layout.addWidget(label1,0,0)
        layout.addWidget(self.user,0,1)
        layout.addWidget(label2,1,0)
        layout.addWidget(self.password,1,1)
        layout.addWidget(boton,2,0)

        self.setLayout(layout)
        boton.clicked.connect(self.press_button)

    def press_button(self):
        if (self.user.text()== "Mario") and (self.password.text() == "1234"):
            print("Bienvenido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    log = login()
    log.show()
    sys.exit(app.exec())