from PyQt5 import QtWidgets, uic, QtMultimedia
import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent

from recurces.lib_thingy.coub_dl import Coub
from recurces.theme import Theme



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self) # Load the .ui file

        self.show() # Show the GUI
        self.downloadbtn.setIcon(QIcon('recurces/quicDownloadBtn.png'))

        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.widget)
        
        
        self.downloadbtn.clicked.connect(self.download)


    def download(self):
        url = self.lineEdit.text()

        coub = Coub()
        coub.audio(url, addlink=True)
        #coub.video(url, addlink=True)
        
        
        coub.lowvideo(url, addlink=False)
        
        self.lineEdit.clear()
        
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "/tmp/tmp.mp4")))
        self.mediaPlayer.play()

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication

app.setStyle("Fusion")
them = Theme()
app.setPalette(them.dark())

window = Ui() # Create an instance of our class
app.exec_() # Start the application
