import sys
import base64
import urllib.parse
from PyQt5.QtWidgets import QMessageBox, QComboBox, QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def url_encode(self):
        try:
            selected_encoding = self.Url_encodeFrom_combo.currentText()
            text = self.Url_encode_field.toPlainText()
            self.Url_result_field.setPlainText(urllib.parse.quote(text.encode(selected_encoding)))
        except UnicodeEncodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def url_decode(self):
        try:
            selected_encoding = self.Url_decodeFrom_combo.currentText()
            text = self.Url_decode_field.toPlainText()
            decoded_bytes = urllib.parse.unquote_to_bytes(text)
            self.Url_result_field.setPlainText(decoded_bytes.decode(selected_encoding))
        except UnicodeDecodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def base64_encode(self):
        try:
            selected_encoding = self.Base64_encodeFrom_combo.currentText()
            text = self.Base64_encode_field.toPlainText()
            sample_string_bytes = text.encode(selected_encoding)
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode(self.Base64_encodeTo_combo.currentText())
            self.Base64_result_field.setPlainText(base64_string)
        except UnicodeEncodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def base64_decode(self):
        try:
            selected_encoding = self.Base64_decodeFrom_combo.currentText()
            text = self.Base64_decode_field.toPlainText()
            sample_string_bytes = text.encode(selected_encoding)
            base64_bytes = base64.b64decode(sample_string_bytes)
            base64_string = base64_bytes.decode(self.Base64_encodeTo_combo.currentText())
            self.Base64_result_field.setPlainText(base64_string)
        except UnicodeDecodeError as ex:
            QMessageBox.information(self, "Info", str(ex))
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PayloadSmith')
        self.setGeometry(100, 100, 800, 600)

        # Set up QTabWidget for tabs
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Add tabs
        self.tab_widget.addTab(self.create_sqli_tab(), "SQLi")
        self.tab_widget.addTab(self.create_xss_tab(), "XSS")
        self.tab_widget.addTab(self.create_url_tab(), "URL")
        self.tab_widget.addTab(self.create_base64_tab(), "Base64")
        self.setWindowIcon(QIcon('logo/logo.png'))
        # Apply QSS for styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #677c91;
                color: white;
                font-family: Arial, sans-serif;
            }
            QTabWidget {
                background-color: #34495e;
                border-radius: 10px;
                font-size: 14px;
                padding: 0;
                margin: 0;
            }
            QTabBar::tab {
                background-color: #34495e;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin: 0 1px;
            }
            QTabBar::tab:selected {
                background-color: #1abc9c;
            }
            QTabWidget::pane {
                border: 2px solid #34495e;
                border-radius: 10px;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #1abc9c;
                border: none;
                color: white;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #16a085;
            }
        """)

    def create_sqli_tab(self):
        sqli_tab = QWidget()
        layout = QVBoxLayout()

        # Add content to SQLi tab
        layout.addWidget(QLabel("SQL Injection Tester"))
        layout.addWidget(QLineEdit())  # Input field for SQL query
        layout.addWidget(QPushButton("Test SQL Injection"))
        sqli_tab.setLayout(layout)
        return sqli_tab

    def create_xss_tab(self):
        xss_tab = QWidget()
        layout = QVBoxLayout()

        # Add content to XSS tab
        layout.addWidget(QLabel("XSS Payload Generator"))
        layout.addWidget(QLineEdit())  # Input field for XSS attack payload
        layout.addWidget(QPushButton("Generate XSS Payload"))
        xss_tab.setLayout(layout)
        return xss_tab

    def create_url_tab(self):
        encodings = ["ascii", "utf-8", "utf-16", "utf-32", "latin-1", "windows-1252","big5", "gbk", "shift_jis", "euc-kr", "iso-8859-5", "iso-8859-6","iso-8859-7", "iso-8859-8", "koi8-r", "mac_roman", "hz", "utf-7","utf-8-sig", "mac_cyrillic", "windows-874", "windows-1250"]
        url_tab = QWidget()
        url_tab.setGeometry(0, 0, 800, 600)
        url_label = QLabel("Url Encoder/Decoder", url_tab)
        url_label.move(10, 10)
        self.Url_encode_field = QTextEdit(url_tab)
        self.Url_encode_field.setGeometry(10, 30, 775, 90) 
        self.Url_encode_field.setStyleSheet("background-color: #dbdbd7;")
        Url_encode_button = QPushButton("Encode Url", url_tab)
        Url_encode_button.setGeometry(610, 115, 175, 45) 
        Url_encode_button.clicked.connect(self.url_encode)
        Url_selectFrom_label = QLabel("Encode from character set :", url_tab)
        Url_selectFrom_label.move(10, 135)
        self.Url_encodeFrom_combo = QComboBox(url_tab)
        self.Url_encodeFrom_combo.addItems(encodings)
        self.Url_encodeFrom_combo.setGeometry(230, 125, 160, 35)
        self.Url_encodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")

        self.Url_decode_field = QTextEdit(url_tab)
        self.Url_decode_field.setGeometry(10, 165, 775, 90)
        self.Url_decode_field.setStyleSheet("background-color: #dbdbd7;")
        Url_decodeSelectFrom_label = QLabel("Decode from character set :", url_tab)
        Url_decodeSelectFrom_label.move(10, 270)
        self.Url_decodeFrom_combo = QComboBox(url_tab)
        self.Url_decodeFrom_combo.addItems(encodings)
        self.Url_decodeFrom_combo.setGeometry(230, 260, 160, 35)
        self.Url_decodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")
        Url_decode_button = QPushButton("Decode Url", url_tab)
        Url_decode_button.setGeometry(610, 250, 175, 45) 
        Url_decode_button.clicked.connect(self.url_decode)
        self.Url_result_field = QTextEdit(url_tab)
        self.Url_result_field.setGeometry(10, 300, 775, 90)
        self.Url_result_field.setText("Encode/Decode Results come here")
        self.Url_result_field.setReadOnly(True)
        self.Url_result_field.setStyleSheet("background-color: #dbdbd7;")
        return url_tab

    def create_base64_tab(self):
        encodings = ["ascii", "utf-8", "utf-16", "utf-32", "latin-1", "windows-1252","big5", "gbk", "shift_jis", "euc-kr", "iso-8859-5", "iso-8859-6","iso-8859-7", "iso-8859-8", "koi8-r", "mac_roman", "hz", "utf-7","utf-8-sig", "mac_cyrillic", "windows-874", "windows-1250"]

        base64_tab = QWidget(self)
        base64_tab.setGeometry(0, 0, 800, 600)
        Base64_label = QLabel("Base64 Encoder/Decoder", base64_tab)
        Base64_label.move(10, 10)
        self.Base64_encode_field = QTextEdit(base64_tab)
        self.Base64_encode_field.setGeometry(10, 30, 775, 90) 
        self.Base64_encode_field.setStyleSheet("background-color: #dbdbd7;")
        Base64_encode_button = QPushButton("Encode Base64", base64_tab)
        Base64_encode_button.setGeometry(610, 115, 175, 45) 
        Base64_selectFrom_label = QLabel("Encode from character set :", base64_tab)
        Base64_selectFrom_label.move(10, 135)
        self.Base64_encodeFrom_combo = QComboBox(base64_tab)
        self.Base64_encodeFrom_combo.addItems(encodings)
        self.Base64_encodeFrom_combo.setGeometry(230, 125, 160, 35)
        self.Base64_encodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")
        Base64_selectTo_label = QLabel("to :", base64_tab)
        Base64_selectTo_label.move(400, 135)
        self.Base64_encodeTo_combo = QComboBox(base64_tab)
        self.Base64_encodeTo_combo.addItems(encodings)
        self.Base64_encodeTo_combo.setGeometry(445, 125, 160, 35)
        self.Base64_encodeTo_combo.setStyleSheet("background-color: #dbdbd7;")
        Base64_encode_button.clicked.connect(self.base64_encode)
        self.Base64_decode_field = QTextEdit(base64_tab)
        self.Base64_decode_field.setGeometry(10, 165, 775, 90)
        self.Base64_decode_field.setStyleSheet("background-color: #dbdbd7;")
        
        Base64_decodeSelectFrom_label = QLabel("Decode from character set :", base64_tab)
        Base64_decodeSelectFrom_label.move(10, 270)
        self.Base64_decodeFrom_combo = QComboBox(base64_tab)
        self.Base64_decodeFrom_combo.addItems(encodings)
        self.Base64_decodeFrom_combo.setGeometry(230, 260, 160, 35)
        self.Base64_decodeFrom_combo.setStyleSheet("background-color: #dbdbd7;")
        Base64_decodeSelectTo_label = QLabel("to :", base64_tab)
        Base64_decodeSelectTo_label.move(400, 270)
        self.Base64_decodeTo_combo = QComboBox(base64_tab)
        self.Base64_decodeTo_combo.addItems(encodings)
        self.Base64_decodeTo_combo.setGeometry(445, 260, 160, 35)
        self.Base64_decodeTo_combo.setStyleSheet("background-color: #dbdbd7;")

        Base64_decode_button = QPushButton("Decode Base64", base64_tab)
        Base64_decode_button.setGeometry(610, 250, 175, 45) 
        Base64_decode_button.clicked.connect(self.base64_decode)
        self.Base64_result_field = QTextEdit(base64_tab)
        self.Base64_result_field.setGeometry(10, 300, 775, 90)
        self.Base64_result_field.setText("Encode/Decode Results come here")
        self.Base64_result_field.setReadOnly(True)
        self.Base64_result_field.setStyleSheet("background-color: #dbdbd7;")
        return base64_tab

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
