import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QHBoxLayout

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(100, 100, 300, 400)

        # Layout principal
        self.layout = QVBoxLayout()

        # Etiqueta para el título
        self.title_label = QLabel("Registro de Tareas")
        self.layout.addWidget(self.title_label)

        # Lista para mostrar las tareas
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Campo de entrada para nuevas tareas
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Introduce una nueva tarea...")
        self.layout.addWidget(self.task_input)

        # Botón para añadir tareas
        self.add_button = QPushButton("Añadir Tarea")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        # Botón para eliminar tareas seleccionadas
        self.remove_button = QPushButton("Eliminar Tarea")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        # Configurar el layout de la ventana principal
        self.setLayout(self.layout)

    def add_task(self):
        # Añadir la tarea a la lista si el campo de entrada no está vacío
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()

    def remove_task(self):
        # Eliminar la tarea seleccionada de la lista
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                self.task_list.takeItem(self.task_list.row(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec_())