import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QGridLayout

class calculadora(QWidget):

    def metodo1():
        pass

    def __init__(self):
        super().__init__()

        self.setWindowTitle("La calculadora")
        self.setGeometry(600,300,300,300)

        self.resultado = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.resultado,0,0,1,4)
        nombre_boton =[["Clear","(",")","/"],
                       ["7","8","9","*"],
                       ["4","5","6","-"],
                       ["1","2","3","+"],
                       ["Delete","0",".","="]]
        #añadir componenetes
        for i in range (1,6):
            for j in range (4):
                boton = QPushButton(nombre_boton[i-1][j])
                layout.addWidget(boton,i,j)
                boton.clicked.connect(self.press_button)
            
        self.setLayout(layout)

    def press_button(self):
        sender = self.sender()
        if (sender.text() == "="):
            self.resultado.setText(str(eval(self.resultado.text())))
        elif (sender.text() == "Clear"):
            self.resultado.clear()
        elif (sender.text() == "Delete"):
            string = self.resultado.text()
            result = QLineEdit(string[:-1])
            self.resultado.setText(str(result.text()))
        else:
            self.resultado.setText((self.resultado.text()) + sender.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)

    calc = calculadora()
    calc.show()
    sys.exit(app.exec())