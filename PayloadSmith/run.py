import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
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
        url_tab = QWidget()
        layout = QVBoxLayout()

        # Add content to URL tab
        layout.addWidget(QLabel("URL Encoder/Decoder"))
        layout.addWidget(QLineEdit())  # Input field for URL
        layout.addWidget(QPushButton("Encode URL"))
        layout.addWidget(QPushButton("Decode URL"))
        url_tab.setLayout(layout)
        return url_tab

    def create_base64_tab(self):
        base64_tab = QWidget(self)
        base64_tab.setGeometry(0, 0, 800, 600)
        Base64_label = QLabel("Base64 Encoder/Decoder", base64_tab)
        Base64_label.move(10, 10)
        Bas64_encode_field = QLineEdit(base64_tab)
        Bas64_encode_field.setGeometry(10, 30, 775, 90) 
        Bas64_encode_field.setStyleSheet("background-color: #dbdbd7;")
        Bas64_encode_button = QPushButton("Encode Base64", base64_tab)
        Bas64_encode_button.setGeometry(610, 115, 175, 45)  
        Bas64_decode_field = QLineEdit(base64_tab)
        Bas64_decode_field.setGeometry(10, 165, 775, 90)
        Bas64_decode_field.setStyleSheet("background-color: #dbdbd7;")
        Bas64_decode_button = QPushButton("Decode Base64", base64_tab)
        Bas64_decode_button.setGeometry(610, 250, 175, 45) 
        Base64_result_field = QTextEdit(base64_tab)
        Base64_result_field.setGeometry(10, 300, 775, 90)
        Base64_result_field.setText("Encode/Decode Results come here")
        Base64_result_field.setReadOnly(True)
        Base64_result_field.setStyleSheet("background-color: #dbdbd7;")
        return base64_tab

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
