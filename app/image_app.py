from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QApplication, QHBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import sys

from app.infection_window import InfectionWindow
from app.report_window import ReportWindow

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Periodontitis")
        self.setFixedSize(600, 700)

        self.model = tf.keras.models.load_model('models/traffic_light_model.h5')
        self.model1 = tf.keras.models.load_model('models/traffic_light_colour_model.h5')
        
        self.picture_label = QLabel("No X-Ray Selected")
        self.picture_label.setAlignment(Qt.AlignCenter)
        self.picture_label.setFixedHeight(400)
        self.picture_label.setStyleSheet("border: 2px solid black")

        self.select_button = QPushButton("Select X-Ray")
        self.select_button.clicked.connect(self.select_image)

        self.clear_button = QPushButton("Clear Selection")
        self.clear_button.setEnabled(False)
        self.clear_button.clicked.connect(self.clear_selection)

        self.infection_button = QPushButton("Infection")
        self.infection_button.setEnabled(False)
        self.infection_button.clicked.connect(self.show_infection_window)

        self.report_button = QPushButton("Make Report")
        self.report_button.setEnabled(False)
        self.report_button.clicked.connect(self.show_report_window)

        font = QFont()
        font.setBold(True)
        font.setPointSize(16)

        self.diag_label = QLabel("")
        self.diag_label.setAlignment(Qt.AlignCenter)
        self.diag_label.setFixedHeight(30)
        self.diag_label.setStyleSheet("border: 1px solid black")

        self.info_label = QLabel("")
        self.info_label.setFixedHeight(30)
        self.info_label.setText("Diagnosis: ")
        self.info_label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.picture_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.diag_label)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.infection_button)
        bottom_layout.addWidget(self.report_button)
        
        layout.addLayout(bottom_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.file_path = ""

    def select_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if self.file_path:
            self.display_image(self.file_path)
            self.display_diag()
            self.clear_button.setEnabled(True)
            self.report_button.setEnabled(True) 

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.picture_label.setPixmap(
            pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def display_diag(self):
        img = image.load_img(self.file_path, target_size=(200, 200))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        val = self.model.predict(images)
        if val[0] == 0:
            self.diag_label.setText("No Traffic Light")
            self.infection_button.setEnabled(False) 
        else:
            val1 = self.model1.predict(images)
            if val1[0] == 0:
                self.diag_label.setText("Green Traffic Light")
                self.infection_button.setEnabled(True) 
            else:
                self.diag_label.setText("Red Traffic Light")
                self.infection_button.setEnabled(True)  

    def clear_selection(self):
        self.picture_label.setText("No X-Ray Selected")
        self.picture_label.setPixmap(QPixmap())
        self.diag_label.setText("")
        self.clear_button.setEnabled(False)
        self.infection_button.setEnabled(False)
        self.report_button.setEnabled(False)

    def show_infection_window(self):
        self.infection_window = InfectionWindow()
        self.infection_window.show()

    def show_report_window(self):
        self.report_window = ReportWindow()
        self.report_window.diagnosis_display.setText(self.diag_label.text())
        self.report_window.set_xray_image_path(self.file_path)
        self.report_window.show()