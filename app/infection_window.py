from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class InfectionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infection Information")
        self.setFixedSize(400, 300)
        layout = QVBoxLayout()
        label = QLabel("Infection details will be shown here.")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
