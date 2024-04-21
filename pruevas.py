import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear un layout vertical
        self.layout = QVBoxLayout()

        # Crear un QLabel para indicar al usuario que escriba algo
        self.label = QLabel('Escribe algo:')
        self.layout.addWidget(self.label)

        # Crear un QLineEdit para la entrada de texto
        self.input_box = QLineEdit()
        self.layout.addWidget(self.input_box)

        # Crear un QPushButton para guardar el texto
        self.boton_guardar = QPushButton('Guardar')
        self.boton_guardar.clicked.connect(self.guardar_texto)
        self.layout.addWidget(self.boton_guardar)

        # Agregar el layout a la ventana
        self.setLayout(self.layout)

        # Configurar las propiedades de la ventana
        self.setWindowTitle('Ejemplo PyQt6')
        self.setGeometry(100, 100, 300, 200)  # Establecer tamaño y posición inicial

    def guardar_texto(self):
        texto_ingresado = self.input_box.text()
        print("Texto ingresado:", texto_ingresado)

if __name__ == '__main__':
    # Crear la aplicación Qt
    app = QApplication(sys.argv)

    # Crear la ventana
    ventana = MiVentana()
    ventana.show()  # Mostrar la ventana

    # Ejecutar la aplicación
    sys.exit(app.exec())
