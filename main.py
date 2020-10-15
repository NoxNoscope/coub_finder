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
		super(Ui, self).__init__()  # Call the inherited classes __init__ method
		uic.loadUi('main_window.ui', self)  # Load the .ui file
		self.downloadbtn.setIcon(QIcon('recurces/quicDownloadBtn.png'))
		
		self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
		self.mediaPlayer.setVideoOutput(self.videowidget)
		
		self.audioCheckBox.setChecked(True)
		
		self.show()  # Show the GUI
		
		self.downloadbtn.clicked.connect(self.download)
		self.restartButton.clicked.connect(self.restart_program)
	
	def download(self):
		url = self.lineEdit.text()
		
		coub = Coub()
		if self.audioCheckBox.isChecked():
			coub.audio(url, addlink=True)
		
		if self.videoCheckBox.isChecked():
			coub.video(url, addlink=True)
		
		coub.lowvideo(url, addlink=False)
		
		self.lineEdit.clear()
		
		self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "/tmp/tmp.mp4")))
		self.mediaPlayer.play()
	
	def restart_program(self):
		"""Restarts the current program, with file objects and descriptors
		   cleanup
		"""
		os.execl(sys.executable, *([sys.executable] + sys.argv))


app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication

app.setStyle("Fusion")  # adding some style that makes more things dark
them = Theme()
app.setPalette(them.dark())  # adding the dark theme thats currently in that file, it can be modified to anything

window = Ui()  # Create an instance of our class
app.exec_()  # Start the application
