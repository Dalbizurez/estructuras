import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit


lista = ['|---------------------------------|']


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear un layout vertical
        self.layout = QVBoxLayout()

        # Crear un botón inicial
        self.input_box = QLineEdit()
        self.boton = QPushButton('Agregar Nodo', self)
        self.boton.clicked.connect(self.agregar_bloque)
        self.boton2 = QPushButton('Eliminar Nodo', self)
        self.boton2.clicked.connect(self.eliminar_1)
        self.boton3 = QPushButton('Buscar Nodo', self)
        self.boton3.clicked.connect(self.buscar_bloque)


        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.boton)
        self.layout.addWidget(self.boton2)
        self.layout.addWidget(self.boton3)

        self.repintar()


        # Agregar el layout a la ventana
        self.setLayout(self.layout)

        # Configurar las propiedades de la ventana
        self.setWindowTitle('Ejemplo PyQt6')
        self.setGeometry(100, 100, 300, 200)  # Establecer tamaño y posición inicial


    def refrescar(self):
        for i in range(len(lista) - 1):
            widget = self.layout.itemAt(self.layout.count() - 1).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()

    def eliminar_1(self):
        if len(lista) - 1:
            widget = self.layout.itemAt(self.layout.count() - len(lista)).widget()
            lista.pop()
            self.layout.removeWidget(widget)
            widget.deleteLater()
        else:
            print('final')


    def repintar(self):
        for i in range(1, len(lista) + 1):
            nuevo_boton = QPushButton(f'{lista[-i]}', self)
            self.layout.addWidget(nuevo_boton)
            nuevo_boton.clicked.connect(self.eliminar_bloque)

    def agregar_bloque(self):
        nume = self.input_box.text()
        lista.append(nume)
        self.refrescar()
        self.repintar()

    def buscar_bloque(self):
        nume = self.input_box.text()
        if nume != '|---------------------------------|':
            cont = 0
            for i in range(1, len(lista) + 1):
                if lista[-i] == nume:
                    break
                cont += 1
            if cont != len(lista):
                self.widget_changed = self.layout.itemAt(self.layout.count() - (len(lista) - cont)).widget()
                self.widget_changed.setStyleSheet("background-color: red;")

    def eliminar_bloque(self):
        # Eliminar el botón que se ha hecho clic
        boton_presionado = self.sender()
        self.layout.removeWidget(boton_presionado)
        boton_presionado.deleteLater()


if __name__ == '__main__':
    # Crear la aplicación Qt
    app = QApplication(sys.argv)

    # Crear la ventana
    ventana = MiVentana()
    ventana.show()  # Mostrar la ventana

    # Ejecutar la aplicación
    sys.exit(app.exec())
