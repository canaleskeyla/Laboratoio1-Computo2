import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Formulario de Datos Personales")
        self.setGeometry(100, 100, 400, 600)  # x, y, ancho, alto

        # Crear un layout para el formulario
        self.form_layout = QFormLayout()

        # Crear campos de entrada para 10 datos
        self.labels = [
            'Nombre Completo', 'Edad', 'Sexo', 'Dirección', 'Teléfono',
            'Correo Electrónico', 'Nacionalidad', 'Ocupación', 'Estado Civil', 'Fecha de Nacimiento'
        ]
        self.inputs = {}

        for label in self.labels:
            field = QLineEdit(self)
            self.form_layout.addRow(QLabel(label), field)
            self.inputs[label] = field

        # Crear un botón para mostrar la información
        self.submit_button = QPushButton("Mostrar Información", self)
        self.submit_button.clicked.connect(self.show_information)

        # Crear un layout vertical
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)

        # Crear una etiqueta para mostrar la información
        self.info_label = QLabel(self)
        main_layout.addWidget(self.info_label)

        # Configurar el layout de la ventana principal
        self.setLayout(main_layout)

    def show_information(self):
        # Recoger la información ingresada
        data = []
        for label in self.labels:
            data.append(f"{label}: {self.inputs[label].text()}")

        # Mostrar la información en la etiqueta
        self.info_label.setText("\n".join(data))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
