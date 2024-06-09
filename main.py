from PySide6.QtWidgets import QApplication,QSlider
from appTest import ImageApp

import sys

app = QApplication(sys.argv)

window = ImageApp()

window.show()
app.exec()