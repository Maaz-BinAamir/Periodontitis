from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        self.picture_label = QLabel("No Image Selected")
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.picture_label.setFixedSize(400, 300)

        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.select_image)

        self.info_label = QLabel("")
        self.info_label.setAlignment(Qt.AlignLeft)
        self.info_label.setFixedHeight(30)

        layout = QVBoxLayout()
        layout.addWidget(self.picture_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.info_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.display_image(file_path)
            self.display_info()

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.picture_label.setPixmap(
            pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def display_info(self):
        self.info_label.setText("Diagnosis: ")
