import sys
from Fare_Harbor_Converter import fareHarborConverter
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class design(QMainWindow):

    def __init__(self):
        super(design, self).__init__()
        self.fhc = fareHarborConverter()
        self.gui_dict_QLabel = {}
        self.gui_dict_QLineEdit = {}
        self.gui_dict_QButton = {}
        self.gui_dict_QTextEdit = {}
        self.m_widget = QWidget()
        self.m_widget.resize(self.m_widget.sizeHint())
        self.setCentralWidget(self.m_widget)
        self.initUI()

    def initUI(self):
        m_layout = QGridLayout()
        self.m_widget.setLayout(m_layout)
        data_groupbox = QGroupBox("Data")
        control_groupbox = QGroupBox("Controls")
        m_layout.addWidget(data_groupbox, 0, 0, QtCore.Qt.AlignTop)
        m_layout.addWidget(control_groupbox,0,1, QtCore.Qt.AlignTop)
        controls_vbox = QVBoxLayout()
        data_g_layout = QGridLayout()
        data_groupbox.setLayout(data_g_layout)
        control_groupbox.setLayout(controls_vbox)

        self.gui_dict_QLabel[1] = QLabel('Open_file', self)
        data_g_layout.addWidget(self.gui_dict_QLabel[1], 0, 0, QtCore.Qt.AlignTop)

        self.gui_dict_QLabel[2] = QLabel('Input Text ', self)
        data_g_layout.addWidget(self.gui_dict_QLabel[2], 1, 0, QtCore.Qt.AlignTop)

        self.gui_dict_QLabel[3] = QLabel('Output Text', self)
        data_g_layout.addWidget(self.gui_dict_QLabel[3], 2, 0, QtCore.Qt.AlignTop)

        self.gui_dict_QLineEdit[1] = QLineEdit('None', self)
        self.gui_dict_QLineEdit[1].setReadOnly(True)
        data_g_layout.addWidget(self.gui_dict_QLineEdit[1], 0, 1, QtCore.Qt.AlignTop)
        self.gui_dict_QLineEdit[1].resize(self.gui_dict_QLineEdit[1].sizeHint())

        self.gui_dict_QTextEdit[1] = QTextEdit("test",self)
        self.gui_dict_QTextEdit[1].setPlainText('Empty ')
        self.gui_dict_QTextEdit[1].setReadOnly(True)
        data_g_layout.addWidget(self.gui_dict_QTextEdit[1], 1, 1, QtCore.Qt.AlignTop)
        self.gui_dict_QTextEdit[1].resize(self.gui_dict_QTextEdit[1].sizeHint())

        self.gui_dict_QTextEdit[2] = QTextEdit("test", self)
        self.gui_dict_QTextEdit[2].setPlainText('Empty ')
        data_g_layout.addWidget(self.gui_dict_QTextEdit[2], 2, 1, QtCore.Qt.AlignTop)
        self.gui_dict_QTextEdit[2].resize(self.gui_dict_QTextEdit[2].sizeHint())

        self.gui_dict_QButton[1] = QPushButton('Open CSV ', self)
        self.gui_dict_QButton[1].resize(self.gui_dict_QButton[1].sizeHint())
        controls_vbox.addWidget(self.gui_dict_QButton[1])
        self.gui_dict_QButton[1].setStyleSheet("background-color: lightgreen;")
        self.gui_dict_QButton[1].clicked.connect(self.button1Clicked)

        self.gui_dict_QButton[2] = QPushButton('Process CSV', self)
        self.gui_dict_QButton[2].resize(self.gui_dict_QButton[2].sizeHint())
        controls_vbox.addWidget(self.gui_dict_QButton[2])
        self.gui_dict_QButton[2].setStyleSheet("background-color: lightblue;")
        self.gui_dict_QButton[2].clicked.connect(self.button2Clicked)

        self.gui_dict_QButton[3] = QPushButton('Save to CSV file', self)
        self.gui_dict_QButton[3].resize(self.gui_dict_QButton[3].sizeHint())
        controls_vbox.addWidget(self.gui_dict_QButton[3])
        self.gui_dict_QButton[3].setStyleSheet("background-color: lightblue;")
        self.gui_dict_QButton[3].clicked.connect(self.button3Clicked)

        self.gui_dict_QButton[4] = QPushButton('Clear Fields', self)
        self.gui_dict_QButton[4].resize(self.gui_dict_QButton[4].sizeHint())
        controls_vbox.addWidget(self.gui_dict_QButton[4])
        self.gui_dict_QButton[4].setStyleSheet("background-color: lightblue;")
        self.gui_dict_QButton[4].clicked.connect(self.button4Clicked)

        self.gui_dict_QButton[5] = QPushButton('QUIT', self)
        self.gui_dict_QButton[5].resize(self.gui_dict_QButton[5].sizeHint())
        controls_vbox.addWidget(self.gui_dict_QButton[5])
        self.gui_dict_QButton[5].setStyleSheet("background-color: red;")
        self.gui_dict_QButton[5].clicked.connect(self.button5Clicked)

        self.statusBar()
        self.statusBar().showMessage('Fare Harbor Converter Started')

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Fare Harbor Convertor')
        self.setStyleSheet("background-color: white;")

        self.show()

    def file_save(self, csv_data):
        file_loc = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(file_loc[0] + ".csv", 'w')
        file.write(csv_data)
        file.close()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def button1Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.statusBar().setStyleSheet("background-color: white;")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Comma Separated Values (*.csv)", options=options)
        if files:
            self.gui_dict_QButton[1].setStyleSheet("background-color: lightblue;")
            self.gui_dict_QButton[2].setStyleSheet("background-color: lightgreen;")
            for file in files:
                self.gui_dict_QLineEdit[1].setText(file)
                if file:
                    with open(file, newline='') as csvfile:
                        self.gui_dict_QTextEdit[1].setText(csvfile.read())


    def button2Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.statusBar().setStyleSheet("background-color: white;")
        if not self.gui_dict_QLineEdit[1].text() == "None":
            self.gui_dict_QButton[2].setStyleSheet("background-color: lightblue;")
            self.gui_dict_QButton[3].setStyleSheet("background-color: lightgreen;")
            tours = self.fhc.get_file_data(self.gui_dict_QLineEdit[1].text())
            text = 'Guest,Tour,Start,End,Driver\n'
            for tour in tours:
                text = text + tour + '\n'
            self.gui_dict_QTextEdit[2].setText(text)
        else:
            self.statusBar().showMessage('Error no file selected')
            self.statusBar().setStyleSheet("background-color: red;")

    def button3Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.statusBar().setStyleSheet("background-color: white;")
        if not self.gui_dict_QLineEdit[1].text() == "None":
            text = self.gui_dict_QTextEdit[2].toPlainText()
            if not text.strip() == 'Empty':
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                      "All Files (*);;Comma Separated Values (*.csv)", options=options)
                if fileName:
                    self.gui_dict_QButton[3].setStyleSheet("background-color: lightblue;")
                    self.gui_dict_QButton[4].setStyleSheet("background-color: lightgreen;")
                    with open(fileName, 'a') as filehandle:
                        filehandle.write(text)
                    self.statusBar().showMessage(f'File saved as {fileName}')
                    self.statusBar().setStyleSheet("background-color: lightgreen;")
                else:
                    self.statusBar().showMessage('Error: No file name written')
                    self.statusBar().setStyleSheet("background-color: red;")
            else:
                self.statusBar().showMessage('Error: No Converted data to save ')
                self.statusBar().setStyleSheet("background-color: red;")
        else:
            self.statusBar().showMessage('Error no file selected')
            self.statusBar().setStyleSheet("background-color: red;")
    def button4Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.statusBar().setStyleSheet("background-color: white;")
        self.gui_dict_QLineEdit[1].setText('None')
        self.gui_dict_QTextEdit[1].setText('Empty')
        self.gui_dict_QTextEdit[2].setText('Empty')
        self.gui_dict_QButton[1].setStyleSheet("background-color: lightgreen;")
        self.gui_dict_QButton[2].setStyleSheet("background-color: lightblue;")
        self.gui_dict_QButton[3].setStyleSheet("background-color: lightblue;")
        self.gui_dict_QButton[4].setStyleSheet("background-color: lightblue;")
        self.statusBar().setStyleSheet("background-color: white;")

    def button5Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.close()

def main():

    app = QApplication(sys.argv)
    ex = design()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
