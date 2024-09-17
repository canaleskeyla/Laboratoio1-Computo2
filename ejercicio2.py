import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Ventana de Clave Secreta")
        self.setGeometry(100, 100, 300, 150)  # x, y, ancho, alto

        # Crear una etiqueta
        self.label = QLabel("Introduce tu clave secreta:", self)

        # Crear un campo de entrada de texto para la clave secreta
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar los caracteres

        # Crear un botón para mostrar la clave secreta ingresada
        self.submit_button = QPushButton("Mostrar Clave", self)
        self.submit_button.clicked.connect(self.show_password)

        # Crear un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)

        # Configurar el layout de la ventana principal
        self.setLayout(layout)

    def show_password(self):
        # Mostrar la clave secreta en una ventana emergente
        password = self.password_input.text()
        QMessageBox.information(self, "Clave Secreta", f"La clave ingresada es: {password}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

