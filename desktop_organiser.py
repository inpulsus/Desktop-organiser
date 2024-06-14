import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt  # Import Qt module from PyQt5.QtCore
import shutil

class DesktopCleaner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Desktop Cleaner')
        self.setGeometry(200, 200, 400, 200)
        self.setStyleSheet('background-color: #2b2b2b; color: #ffffff;')

        self.label = QLabel('Click to organize your desktop:', self)
        self.label.setFont(QFont('Arial', 16))
        self.label.setAlignment(Qt.AlignCenter)  # Align label text to the center using Qt.AlignCenter

        self.btn_clean = QPushButton('Clean Desktop', self)
        self.btn_clean.setFont(QFont('Arial', 14))
        self.btn_clean.setStyleSheet('padding: 10px; background-color: #1e90ff; color: #ffffff; border: none;')
        self.btn_clean.clicked.connect(self.clean_desktop)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)  # Align label vertically and horizontally centered
        vbox.addWidget(self.btn_clean, alignment=Qt.AlignCenter)  # Align button vertically and horizontally centered
        self.setLayout(vbox)

    def clean_desktop(self):
        desktop_path = os.path.expanduser("~/Desktop")
        folders_to_create = []

        # Check for file types and add corresponding folder names to folders_to_create
        if any(file.endswith(('.txt', '.doc', '.docx', '.pdf', '.xlsx', '.xls')) for file in os.listdir(desktop_path)):
            folders_to_create.append('Text Documents')

        if any(file.endswith(('.jpg', '.jpeg', '.png', '.gif')) for file in os.listdir(desktop_path)):
            folders_to_create.append('Pictures')

        if any(file.endswith(('.mp4', '.avi', '.mov', '.mkv')) for file in os.listdir(desktop_path)):
            folders_to_create.append('Videos')

        if any(file.endswith(('.mp3', '.wav', '.ogg')) for file in os.listdir(desktop_path)):
            folders_to_create.append('Sounds')

        if any(file.endswith(('.7z', '.rar')) for file in os.listdir(desktop_path)):
            folders_to_create.append('Zipped files')

        # Create folders only if they are needed
        for folder_name in folders_to_create:
            folder_path = os.path.join(desktop_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        # Move files into their respective folders
        desktop_files = os.listdir(desktop_path)

        for file_name in desktop_files:
            if file_name.lower().endswith(('.txt', '.doc', '.docx', '.pdf', '.xlsx', '.xls')):
                source_path = os.path.join(desktop_path, file_name)
                destination_path = os.path.join(desktop_path, 'Text Documents', file_name)
                shutil.move(source_path, destination_path)
            elif file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                source_path = os.path.join(desktop_path, file_name)
                destination_path = os.path.join(desktop_path, 'Pictures', file_name)
                shutil.move(source_path, destination_path)
            elif file_name.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                source_path = os.path.join(desktop_path, file_name)
                destination_path = os.path.join(desktop_path, 'Videos', file_name)
                shutil.move(source_path, destination_path)
            elif file_name.lower().endswith(('.mp3', '.wav', '.ogg')):
                source_path = os.path.join(desktop_path, file_name)
                destination_path = os.path.join(desktop_path, 'Sounds', file_name)
                shutil.move(source_path, destination_path)
            elif file_name.lower().endswith(('.7z', '.rar')):
                source_path = os.path.join(desktop_path, file_name)
                destination_path = os.path.join(desktop_path, 'Zipped files', file_name)
                shutil.move(source_path, destination_path)

        self.label.setText('Desktop cleaned successfully!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DesktopCleaner()
    ex.show()
    sys.exit(app.exec_())
