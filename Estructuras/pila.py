import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
from guardado import cargar_lista, guardar_lista

lista = ['\nFinal\n']


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.layout = QHBoxLayout()
        self.layout2 = QVBoxLayout()

        self.input_box = QLineEdit()
        self.boton = QPushButton('Agregar Nodo', self)
        self.boton.clicked.connect(self.agregar_bloque)
        self.boton2 = QPushButton('Eliminar Nodo', self)
        self.boton2.clicked.connect(self.eliminar_1)
        self.boton3 = QPushButton('Buscar Nodo Por ID', self)
        self.boton3.clicked.connect(self.buscar_bloque)
        self.boton4 = QPushButton('Guardar', self)
        self.boton4.clicked.connect(self.guardar)
        self.boton5 = QPushButton('\tCargar\t', self)
        self.boton5.clicked.connect(self.cargar)

        self.layout2.addWidget(self.input_box)
        self.layout2.addWidget(self.boton)
        self.layout2.addWidget(self.boton2)
        self.layout2.addWidget(self.boton3)
        self.layout2.addWidget(self.boton4)
        self.layout2.addWidget(self.boton5)



        self.layout.addLayout(self.layout2)

        self.setLayout(self.layout)

        self.repintar()


        self.setWindowTitle('Ejemplo PyQt6')
        self.setGeometry(100, 100, 300, 100)




    def refrescar(self):
        print(lista)
        for i in range(len(lista) - 1):
            widget = self.layout.itemAt(self.layout.count() - 1).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()
            self.setGeometry(100, 100, 300, 100)



    def eliminar_1(self):
        for x in range(2):
            if len(lista) - 1:
                widget = self.layout.itemAt(self.layout.count() - len(lista)).widget()
                lista.pop()
                self.layout.removeWidget(widget)
                widget.deleteLater()
            else:
                print('Final')


    def repintar(self):
        for i in range(1, len(lista) + 1):
            nuevo_boton = QPushButton(f'{lista[-i]}', self)
            self.layout.addWidget(nuevo_boton)




    def agregar_bloque(self):
        self.agregar_flecha()
        print(lista[-1], id(lista[-1]))
        nume = 'Nodo: ' + self.input_box.text() + '\nEspacio de memoria:\n' + str(id(lista[-2]))
        lista.append(nume)
        self.refrescar()
        self.repintar()


    def agregar_flecha(self):
        lista.append('\n-->\n')
        self.refrescar()
        self.repintar()


    def buscar_bloque(self):
        nume = self.input_box.text()
        cont = 0
        for i in range(1, len(lista) + 1):
            if str(lista[-i])[-13:] == nume:
                break
            cont += 1
        if cont != len(lista):
            self.widget_changed = self.layout.itemAt(self.layout.count() - (len(lista) - cont)).widget()
            self.widget_changed.setStyleSheet("background-color: red;")

    def eliminar_bloque(self):
        boton_presionado = self.sender()
        self.layout.removeWidget(boton_presionado)
        boton_presionado.deleteLater()

#guardados

    def guardar(self):
        guardar_lista(lista, self.input_box.text())

    def limpiar(self):
        for i in range(len(lista)):
            widget = self.layout.itemAt(self.layout.count() - 1).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()
            self.setGeometry(100, 100, 300, 100)

    def cargar(self):
        self.limpiar()
        lista.clear()
        self.repintar()
        for i in cargar_lista(str(self.input_box.text())):
            lista.append(str(i))

        self.repintar()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
