from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateTimeEdit, QHBoxLayout, QFormLayout, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QPixmap
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class ReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Report")
        self.setFixedSize(600, 600)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignLeft)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignLeft)

        self.name_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)

        self.age_input = QLineEdit()
        form_layout.addRow("Age:", self.age_input)

        self.token_input = QLineEdit()
        form_layout.addRow("Token Number:", self.token_input)

        self.datetime_label = QLabel("Date:")
        self.datetime_display_date = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_display_date.setDisplayFormat("yyyy-MM-dd")
        self.datetime_display_date.setReadOnly(True)
        self.datetime_display_date.setButtonSymbols(QDateTimeEdit.NoButtons)
        form_layout.addRow(self.datetime_label, self.datetime_display_date)

        self.time_label = QLabel("Time:")
        self.datetime_display_time = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_display_time.setDisplayFormat("HH:mm:ss")
        self.datetime_display_time.setReadOnly(True)
        self.datetime_display_time.setButtonSymbols(QDateTimeEdit.NoButtons)
        form_layout.addRow(self.time_label, self.datetime_display_time)

        self.diagnosis_display = QLabel("")
        form_layout.addRow("Diagnosis:", self.diagnosis_display)

        self.xray_label = QLabel("X-ray:")
        self.xray_image_label = QLabel() 
        form_layout.addRow(self.xray_label, self.xray_image_label)

        layout.addLayout(form_layout)

        self.export_button = QPushButton("Export")
        self.export_button.setEnabled(False)
        self.export_button.clicked.connect(self.export_to_pdf)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.export_button)
        layout.addLayout(button_layout)

        self.name_input.textChanged.connect(self.check_fields_filled)
        self.age_input.textChanged.connect(self.check_fields_filled)
        self.token_input.textChanged.connect(self.check_fields_filled)

        self.setLayout(layout)

        font_size = self.name_input.font().pointSize()
        self.heading_style = ParagraphStyle(name='Heading1', parent=getSampleStyleSheet()['Heading1'],
                                            fontSize=font_size, leading=font_size)

        self.xray_image_path = None  # Variable to store the path of the X-ray image

    def check_fields_filled(self):
        if self.name_input.text() and self.age_input.text() and self.token_input.text():
            self.export_button.setEnabled(True)
        else:
            self.export_button.setEnabled(False)

    def set_xray_image(self, file_path):
        self.xray_image_path = file_path  # Store the path of the X-ray image
        pixmap = QPixmap(file_path)
        self.xray_image_label.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))

    def set_xray_image_path(self, image_path):
        self.set_xray_image(image_path)

    def generate_pdf(self, file_path):
        name = self.name_input.text()
        age = self.age_input.text()
        token_number = self.token_input.text()
        date = self.datetime_display_date.dateTime().toString("yyyy-MM-dd")
        time = self.datetime_display_time.dateTime().toString("HH:mm:ss")
        diagnosis = self.diagnosis_display.text()

        file_name = f"{name}-{age}-{token_number}-{date}.pdf"

        doc = SimpleDocTemplate(file_path + "/" + file_name, pagesize=letter)
        styles = getSampleStyleSheet()
        styleN = styles['Normal']

        elements = []

        elements.append(Paragraph('Periodontitis', ParagraphStyle(name='Center', alignment=1, fontSize=16, fontName='Helvetica-Bold')))
        elements.append(Spacer(1, 12))

        data = [
            [Paragraph('Name', self.heading_style), name],
            [Paragraph('Age', self.heading_style), age],
            [Paragraph('Token Number', self.heading_style), token_number],
            [Paragraph('Date', self.heading_style), date],
            [Paragraph('Time', self.heading_style), time],
            [Paragraph('Diagnosis', self.heading_style), diagnosis]
        ]

        table = Table(data, colWidths=[110, 390])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.black)
        ]))

        elements.append(table)
        elements.append(Spacer(1, 12))

        if self.xray_image_path:
            elements.append(Paragraph('X-ray', self.heading_style))
            elements.append(Spacer(1, 12))
            try:
                elements.append(Image(self.xray_image_path, width=400, height=300))
            except Exception as e:
                elements.append(Paragraph(f"Error loading image: {str(e)}", styleN))

        def draw_border(canvas, doc):
            width, height = doc.pagesize
            canvas.setLineWidth(0.5)
            canvas.setStrokeColor(colors.black)
            canvas.rect(10, 10, width - 20, height - 20)  

        doc.build(elements, onFirstPage=draw_border, onLaterPages=draw_border)

        QMessageBox.information(self, "Success", "File exported successfully.")
        self.close()

    def export_to_pdf(self):
        file_path = QFileDialog.getExistingDirectory(self, "Save PDF", "")
        if file_path:
            self.generate_pdf(file_path)
