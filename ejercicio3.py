import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Formulario de Información")
        self.setGeometry(100, 100, 400, 200)  # x, y, ancho, alto

        # Crear etiquetas
        self.cedula_label = QLabel("Número de Cédula:", self)
        self.nombre_label = QLabel("Nombre Completo:", self)

        # Crear campos de entrada de texto
        self.cedula_input = QLineEdit(self)
        self.nombre_input = QLineEdit(self)

        # Crear un botón para mostrar la información
        self.submit_button = QPushButton("Mostrar Información", self)
        self.submit_button.clicked.connect(self.show_information)

        # Crear un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.cedula_input, alignment=Qt.AlignLeft)
        layout.addWidget(self.nombre_label, alignment=Qt.AlignLeft)
        layout.addWidget(self.nombre_input, alignment=Qt.AlignLeft)
        layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)

        # Configurar el layout de la ventana principal
        self.setLayout(layout)

    def show_information(self):
        # Obtener la información ingresada
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        
        # Mostrar la información en una ventana emergente
        QMessageBox.information(self, "Información Ingresada", f"Número de Cédula: {cedula}\nNombre Completo: {nombre}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
