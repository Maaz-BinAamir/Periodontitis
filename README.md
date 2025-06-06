# Periodontitis

Overview
The Image Viewer application is a simple graphical user interface (GUI) tool built using PySide6. It allows users to select an image file from their system, display the image within the application, and show a placeholder for diagnostic information.

Features
Select Image: Users can select an image file (PNG, JPG, JPEG, BMP, GIF) from their file system.

Display Image: The selected image is displayed within the application window.

Diagnostic Placeholder: A label is available to display diagnostic information related to the image.

Installation
Clone the repository:

git clone <repository_url>
cd <repository_directory>
Install dependencies:
Ensure you have PySide6 installed. You can install it using pip:

pip install PySide6

Usage
Run the application:

python image_viewer.py
Replace image_viewer.py with the filename of your script if it is named differently.

Select an image:

Click the "Select Image" button.
Choose an image file from the file dialog.
The selected image will be displayed in the application window.
Code Overview
Main Window Class

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        ...
The ImageApp class inherits from QMainWindow and sets up the main window for the application. It initializes the UI components and connects the button click event to the select_image method.

Select Image Method

def select_image(self):
    file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
    if file_path:
        self.display_image(file_path)
        self.display_info()
The select_image method opens a file dialog for the user to select an image file. If a file is selected, it calls the display_image and display_info methods.

Display Image Method

def display_image(self, file_path):
    pixmap = QPixmap(file_path)
    self.picture_label.setPixmap(
        pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
The display_image method takes the file path of the selected image, loads it into a QPixmap, and displays it in the picture_label.

Display Info Method

def display_info(self):
    self.info_label.setText("Diagnosis: ")
The display_info method updates the info_label to display a placeholder for diagnostic information. This can be expanded to include actual diagnostic data as needed.

Dependencies
Python 3.x
PySide6
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
PySide6 documentation and tutorials.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

Contact
For any questions or issues, please open an issue in the repository or contact the maintainer.
