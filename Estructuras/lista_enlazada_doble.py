import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
from guardado import cargar_lista, guardar_lista

lista = ['\nCola\n']


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.layout = QHBoxLayout()
        self.layout2 = QVBoxLayout()


        self.input_box = QLineEdit()
        self.input_box2 = QLineEdit()
        self.input_box3 = QLineEdit()

        self.boton = QPushButton('Agregar Nodo Al Inicio', self)
        self.boton.clicked.connect(self.agregar_final)
        self.boton_1 = QPushButton('Agregar Nodo Al Final', self)
        self.boton_1.clicked.connect(self.agregar_inicio)
        self.boton_2 = QPushButton('Agregar Nodo Por Posicion', self)
        self.boton_2.clicked.connect(self.verificar_num)
        self.boton2 = QPushButton('Eliminar Nodo Al Final', self)
        self.boton2.clicked.connect(self.eliminar_derecha)
        self.boton2_1 = QPushButton('Eliminar Nodo Al Inicio', self)
        self.boton2_1.clicked.connect(self.eliminar_izquierda)
        self.boton2_2 = QPushButton('Eliminar Nodo Por Posicion', self)
        self.boton2_2.clicked.connect(self.verificar_num2)
        self.boton3 = QPushButton('Buscar Nodo Por ID', self)
        self.boton3.clicked.connect(self.buscar_bloque)
        self.boton4 = QPushButton('Guardar', self)
        self.boton4.clicked.connect(self.guardar)
        self.boton5 = QPushButton('\tCargar\t', self)
        self.boton5.clicked.connect(self.cargar)

        self.layout2.addWidget(self.input_box)
        self.layout2.addWidget(self.boton)
        self.layout2.addWidget(self.boton_1)
        self.layout2.addWidget(self.boton2_1)
        self.layout2.addWidget(self.boton2)
        self.layout2.addWidget(self.boton3)
        self.layout2.addWidget(self.input_box2)
        self.layout2.addWidget(self.boton_2)
        self.layout2.addWidget(self.boton2_2)
        self.layout2.addWidget(self.input_box3)
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



    def eliminar_izquierda(self):
        for x in range(2):
            if len(lista) - 1:
                widget = self.layout.itemAt(self.layout.count() - len(lista)).widget()
                lista.pop()
                self.layout.removeWidget(widget)
                widget.deleteLater()
            else:
                print('Final')

    def eliminar_derecha(self):
        for x in range(2):
            if len(lista) - 1:
                widget = self.layout.itemAt(self.layout.count() - 2).widget()
                lista.remove(lista[1])
                self.layout.removeWidget(widget)
                widget.deleteLater()
            else:
                print('Final')


    def repintar(self):
        for i in range(1, len(lista) + 1):
            nuevo_boton = QPushButton(f'{lista[-i]}', self)
            self.layout.addWidget(nuevo_boton)
            self.setGeometry(100, 100, 300, 100)




    def agregar_inicio(self):
        self.agregar_flecha_inicio()
        print(lista[-1], id(lista[-2]))
        if len(lista) == 2:
            nume = 'Nodo: ' + self.input_box.text() + '\nEspacio de memoria:\n' + str(id(lista[0]))
        elif len(lista) == 4:
            nume = 'Nodo: ' + self.input_box.text() + '\nEspacio de memoria:\n' + str(id(lista[-1]))
        else:
            nume = 'Nodo: ' + self.input_box.text() + '\nEspacio de memoria:\n' + str(id(lista[3]))
        lista.insert(2, nume)

        self.refrescar()
        self.repintar()

    def agregar_flecha_inicio(self):
        lista.insert(1, '\n<-->\n')
        self.refrescar()
        self.repintar()

    def agregar_final(self):
        self.agregar_flecha_final()
        nume = 'Nodo: ' + self.input_box.text() + '\nEspacio de memoria:\n' + str(id(lista[-2]))
        lista.append(nume)
        self.refrescar()
        self.repintar()


    def agregar_flecha_final(self):
        lista.append('\n<-->\n')
        self.refrescar()
        self.repintar()

    def verificar_num(self):
        nume2 = self.input_box.text()
        nume = self.input_box2.text()
        try:
            if int(nume):
                print('entro a verificar', nume2)
            self.agregar_en()

        except(ValueError):
            print('Valor incomoresible', nume)

    def verificar_num2(self):
        nume = self.input_box2.text()
        try:
            if int(nume):
                print('entro a verificar')
            self.eliminar_en()
        except(ValueError):
            print('Valor incomoresible', nume)

    def eliminar_en(self):
        nume = int(self.input_box2.text())
        if nume == 0:
            self.eliminar_izquierda()
        elif nume >= ((len(lista) - 1) / 2):
            self.eliminar_derecha()
        else:
            self.eliminar_sobras()
            for i in range(2):
                lista.pop(-(nume * 2))
            self.refrescar()
            widget = self.layout.itemAt(self.layout.count() - 1).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()
            self.repintar()



    def eliminar_sobras(self):
        for i in range(2):
            widget = self.layout.itemAt(self.layout.count() - 1).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()



    def agregar_en(self):
        nume = int(self.input_box2.text())
        if nume == 0:
            self.agregar_final()
        elif nume >= ((len(lista) - 1) / 2):
            self.agregar_inicio()
        else:
            agregado = self.input_box.text()
            print(agregado)
            self.agregar_texto_en()
            lista.insert(-((nume * 2)), 'Nodo: ' + str(agregado) + '\nEspacio de memoria:\n' + str(id(lista[nume])))
            self.refrescar()
            self.repintar()

    def agregar_texto_en(self):
        nume = int(self.input_box2.text())
        lista.insert(-((nume * 2) ), '\n<-->\n')
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
        guardar_lista(lista, self.input_box3.text())

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
        for i in cargar_lista(str(self.input_box3.text())):
            lista.append(str(i))

        self.repintar()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())