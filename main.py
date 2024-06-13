from PySide6.QtWidgets import QApplication,QSlider
from app.image_app import ImageApp

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec())
