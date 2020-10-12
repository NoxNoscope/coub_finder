from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from coub_dl import Coub
from theme import Theme



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self) # Load the .ui file

        self.show() # Show the GUI
        self.downloadbtn.setIcon(QIcon('quicDownloadBtn.png'))
        
        self.downloadbtn.clicked.connect(self.download)


    def download(self):
        url = self.lineEdit.text()

        coub = Coub()
        coub.audio(url, addlink=True)
        
        self.lineEdit.clear()


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication

app.setStyle("Fusion")
them = Theme()
app.setPalette(them.dark())

window = Ui() # Create an instance of our class
app.exec_() # Start the application
