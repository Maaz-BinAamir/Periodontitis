from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import sys

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Periodontitis")
        self.setFixedSize(600, 600)

        self.picture_label = QLabel("No X-Ray Selected")
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.picture_label.setFixedHeight(400)
        self.picture_label.setStyleSheet("border: 2px solid black")

        self.select_button = QPushButton("Select X-Ray")
        self.select_button.clicked.connect(self.select_image)

        self.clear_button = QPushButton("Clear Selection")
        self.clear_button.setEnabled(False)  
        self.clear_button.clicked.connect(self.clear_selection)

        font = QFont()
        font.setBold(True)
        font.setPointSize(16)

        self.diag_label = QLabel("")
        self.diag_label.setAlignment(Qt.AlignCenter)
        self.diag_label.setFixedHeight(30) 

        self.info_label = QLabel("")
        self.info_label.setFixedHeight(30) 
        self.info_label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.picture_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.clear_button)  
        layout.addWidget(self.info_label)
        layout.addWidget(self.diag_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.display_image(file_path)
            self.display_info()
            self.display_diag()
            self.clear_button.setEnabled(True)  

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.picture_label.setPixmap(
            pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def display_info(self):
        self.info_label.setText("Diagnosis: ")
        self.diag_label.setStyleSheet("border: 1px solid black")

    def display_diag(self):
        self.diag_label.setText("Apical Periodontitis")

    def clear_selection(self):
        self.picture_label.setText("No X-Ray Selected")
        self.picture_label.setPixmap(QPixmap()) 
        self.info_label.setText("")
        self.diag_label.setText("")
        self.diag_label.setStyleSheet("")  
        self.clear_button.setEnabled(False)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec())