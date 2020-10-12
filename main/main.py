from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import *
from main.recurces.lib_thingy.coub_dl import Coub
from main.recurces.theme import Theme



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self) # Load the .ui file

        self.show() # Show the GUI
        self.downloadbtn.setIcon(QIcon('recurces/quicDownloadBtn.png'))
        
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
