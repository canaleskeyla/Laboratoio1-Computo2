import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Ventana de Información")
        self.setGeometry(100, 100, 300, 200)  # x, y, ancho, alto

        # Crear etiquetas para nombre completo y edad
        self.name_label = QLabel("Nombre Completo: Keila Nallely Canales", self)
        self.age_label = QLabel("Edad: 20 años", self)

        # Crear un layout vertical para centrar el contenido
        layout = QVBoxLayout()
        layout.addWidget(self.name_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.age_label, alignment=Qt.AlignCenter)

        # Configurar el layout de la ventana principal
        self.setLayout(layout)

        # Ajustar el layout para centrar todo verticalmente
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Ventana de Información")

        # Ajustar el tamaño del contenido para centrado vertical
        self.setFixedSize(self.sizeHint())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
