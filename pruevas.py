import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear un layout vertical
        self.layout = QVBoxLayout()

        # Crear un botón
        self.boton = QPushButton('Cambiar color', self)
        self.boton.clicked.connect(self.cambiar_color)
        self.layout.addWidget(self.boton)

        # Agregar el layout a la ventana
        self.setLayout(self.layout)

        # Configurar las propiedades de la ventana
        self.setWindowTitle('Cambiar color de un botón')
        self.setGeometry(100, 100, 300, 200)  # Establecer tamaño y posición inicial

    def cambiar_color(self):
        self.boton.setStyleSheet("background-color: red;")

if __name__ == '__main__':
    # Crear la aplicación Qt
    app = QApplication(sys.argv)

    # Crear la ventana
    ventana = MiVentana()
    ventana.show()  # Mostrar la ventana

    # Ejecutar la aplicación
    sys.exit(app.exec())
