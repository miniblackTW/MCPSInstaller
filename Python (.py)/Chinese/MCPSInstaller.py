import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QProgressBar

versions_data = {
    "latest": "1.21",
    "versions": {
        "1.21": "https://api.papermc.io/v2/projects/paper/versions/1.21/builds/91/downloads/paper-1.21-91.jar",
        "1.20.6": "https://api.papermc.io/v2/projects/paper/versions/1.20.6/builds/148/downloads/paper-1.20.6-148.jar",
        "1.20.5": "https://api.papermc.io/v2/projects/paper/versions/1.20.5/builds/22/downloads/paper-1.20.5-22.jar",
        "1.20.4": "https://api.papermc.io/v2/projects/paper/versions/1.20.4/builds/497/downloads/paper-1.20.4-497.jar",
        "1.20.2": "https://api.papermc.io/v2/projects/paper/versions/1.20.2/builds/318/downloads/paper-1.20.2-318.jar",
        "1.20.1": "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/196/downloads/paper-1.20.1-196.jar",
        "1.20": "https://api.papermc.io/v2/projects/paper/versions/1.20/builds/17/downloads/paper-1.20-17.jar",
        "1.19.4": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
        "1.19.3": "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/448/downloads/paper-1.19.3-448.jar",
        "1.19.2": "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/307/downloads/paper-1.19.2-307.jar",
        "1.19.1": "https://api.papermc.io/v2/projects/paper/versions/1.19.1/builds/111/downloads/paper-1.19.1-111.jar",
        "1.19": "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/81/downloads/paper-1.19-81.jar",
        "1.18.2": "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar",
        "1.18.1": "https://api.papermc.io/v2/projects/paper/versions/1.18.1/builds/216/downloads/paper-1.18.1-216.jar",
        "1.18": "https://api.papermc.io/v2/projects/paper/versions/1.18/builds/66/downloads/paper-1.18-66.jar",
        "1.17.1": "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar",
        "1.17": "https://api.papermc.io/v2/projects/paper/versions/1.17/builds/79/downloads/paper-1.17-79.jar",
        "1.16.5": "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
        "1.16.4": "https://api.papermc.io/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar",
        "1.16.3": "https://api.papermc.io/v2/projects/paper/versions/1.16.3/builds/253/downloads/paper-1.16.3-253.jar",
        "1.16.2": "https://api.papermc.io/v2/projects/paper/versions/1.16.2/builds/189/downloads/paper-1.16.2-189.jar",
        "1.16.1": "https://api.papermc.io/v2/projects/paper/versions/1.16.1/builds/138/downloads/paper-1.16.1-138.jar",
        "1.15.2": "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar",
        "1.15.1": "https://api.papermc.io/v2/projects/paper/versions/1.15.1/builds/62/downloads/paper-1.15.1-62.jar",
        "1.15": "https://api.papermc.io/v2/projects/paper/versions/1.15/builds/21/downloads/paper-1.15-21.jar",
        "1.14.4": "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar",
        "1.14.3": "https://api.papermc.io/v2/projects/paper/versions/1.14.3/builds/134/downloads/paper-1.14.3-134.jar",
        "1.14.2": "https://api.papermc.io/v2/projects/paper/versions/1.14.2/builds/107/downloads/paper-1.14.2-107.jar",
        "1.14.1": "https://api.papermc.io/v2/projects/paper/versions/1.14.1/builds/50/downloads/paper-1.14.1-50.jar",
        "1.14": "https://api.papermc.io/v2/projects/paper/versions/1.14/builds/17/downloads/paper-1.14-17.jar",
        "1.13.2": "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar",
        "1.13.1": "https://api.papermc.io/v2/projects/paper/versions/1.13.1/builds/386/downloads/paper-1.13.1-386.jar",
        "1.13": "https://api.papermc.io/v2/projects/paper/versions/1.13/builds/173/downloads/paper-1.13-173.jar",
        "1.13-pre7": "https://api.papermc.io/v2/projects/paper/versions/1.13-pre7/builds/12/downloads/paper-1.13-pre7-12.jar",
        "1.12.2": "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
        "1.12.1": "https://api.papermc.io/v2/projects/paper/versions/1.12.1/builds/1204/downloads/paper-1.12.1-1204.jar",
        "1.12": "https://api.papermc.io/v2/projects/paper/versions/1.12/builds/1169/downloads/paper-1.12-1169.jar",
        "1.11.2": "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar",
        "1.10.2": "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar",
        "1.9.4": "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar",
        "1.8.8": "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar"
    }
}

class Installer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minecraft Paper 伺服器安裝')

        self.version_label = QLabel('選擇 Minecraft 版本:', self)
        self.version_combo = QComboBox(self)
        self.version_combo.addItems(versions_data['versions'].keys())

        self.folder_button = QPushButton('選擇要安裝伺服器的資料夾', self)
        self.folder_button.clicked.connect(self.select_folder)
        self.folder_label = QLabel('', self)

        self.install_button = QPushButton('安裝伺服器', self)
        self.install_button.clicked.connect(self.install_server)
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)

        layout = QVBoxLayout()
        layout.addWidget(self.version_label)
        layout.addWidget(self.version_combo)
        layout.addWidget(self.folder_button)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.install_button)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
        self.selected_folder = None

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, '選擇資料夾')
        if folder:
            self.selected_folder = folder
            self.folder_label.setText(folder)

    def install_server(self):
        version = self.version_combo.currentText()
        url = versions_data['versions'][version]

        if self.selected_folder is None:
            QMessageBox.warning(self, '錯誤', '請選擇一個資料夾')
            return

        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.download_file(url, self.selected_folder, f'server.jar')

    def download_file(self, url, folder, filename):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress = 0

        with open(os.path.join(folder, filename), 'wb') as file:
            for data in response.iter_content(block_size):
                progress += len(data)
                file.write(data)
                self.progress_bar.setValue(int(progress * 100 / total_size))
                self.create_start_bat(folder, filename)

        self.create_start_bat(folder, filename)

        QMessageBox.information(self, '成功', '伺服器安裝成功')

    def create_start_bat(self, folder, filename):
        bat_content = f"java -Xmx1024M -Xms512M -jar {filename} nogui"
        bat_path = os.path.join(folder, 'start.bat')
        
        with open(bat_path, 'w') as bat_file:
            bat_file.write(bat_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    installer = Installer()
    installer.show()
    sys.exit(app.exec_())
