import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QFormLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Formulario de Mascotas")
        self.setGeometry(100, 100, 400, 400)  # x, y, ancho, alto

        # Crear etiquetas y campos de entrada para 3 mascotas
        self.labels = ['Nombre', 'Especie', 'Edad']
        self.inputs = {}
        self.create_input_fields()

        # Crear un botón para mostrar la información
        self.submit_button = QPushButton("Mostrar Información", self)
        self.submit_button.clicked.connect(self.show_information)

        # Crear un layout vertical
        main_layout = QVBoxLayout()

        # Añadir el formulario al layout principal
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)

        # Configurar el layout de la ventana principal
        self.setLayout(main_layout)

    def create_input_fields(self):
        # Crear un formulario para cada mascota
        self.form_layout = QFormLayout()

        for i in range(1, 4):
            self.form_layout.addRow(QLabel(f"Mascota {i}: Nombre"), QLineEdit())
            self.form_layout.addRow(QLabel(f"Mascota {i}: Especie"), QLineEdit())
            self.form_layout.addRow(QLabel(f"Mascota {i}: Edad"), QLineEdit())

        # Guardar los campos en un diccionario para acceder a ellos fácilmente
        self.inputs['mascota1'] = [self.form_layout.itemAt(i, QFormLayout.FieldRole).widget() for i in range(0, 3)]
        self.inputs['mascota2'] = [self.form_layout.itemAt(i, QFormLayout.FieldRole).widget() for i in range(3, 6)]
        self.inputs['mascota3'] = [self.form_layout.itemAt(i, QFormLayout.FieldRole).widget() for i in range(6, 9)]

    def show_information(self):
        # Recoger la información ingresada
        data = []
        for key in self.inputs:
            data.append(f"Mascota {key[-1]}:\n")
            data.append(f"Nombre: {self.inputs[key][0].text()}\n")
            data.append(f"Especie: {self.inputs[key][1].text()}\n")
            data.append(f"Edad: {self.inputs[key][2].text()}\n\n")

        # Mostrar la información en una ventana emergente
        QMessageBox.information(self, "Información de Mascotas", ''.join(data))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())