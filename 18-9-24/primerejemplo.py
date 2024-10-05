from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

app=QApplication(sys.argv)

mapp=QMainWindow()
mapp.show()

ventana=QWidget()
ventana.show()

boton=QPushButton("Boton rojo")
boton.show()

app.exec()
