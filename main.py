from PyQt5 import QtWidgets, uic, QtMultimedia
import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent
import yaml

from recurces.lib_thingy.coub_dl import Coub
from recurces.theme import Theme


class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		self.setting = self.yaml_load()
		
		super(Ui, self).__init__()  # Call the inherited classes __init__ method
		uic.loadUi('main_window.ui', self)  # Load the .ui file
		self.downloadbtn.setIcon(QIcon('recurces/quicDownloadBtn.png'))
		
		self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
		self.mediaPlayer.setVideoOutput(self.videowidget)
		
		self.audioCheckBox.setChecked(self.setting["audioCheckBox"])
		self.videoCheckBox.setChecked(self.setting["videoCheckBox"])
		self.previewCheckBox.setChecked(self.setting["previewCheckBox"])
		
		self.show()  # Show the GUI
		
		self.downloadbtn.clicked.connect(self.download)
		self.restartButton.clicked.connect(self.restart_program)
		self.audioCheckBox.stateChanged.connect(self.audioCheckBox_toggle)
		self.videoCheckBox.stateChanged.connect(self.videoCheckBox_toggle)
		self.previewCheckBox.stateChanged.connect(self.previewCheckBox_toggle)
	
	def download(self):
		"""
		downloads the selected files and clears lineeddit, and displays a small preview
		"""
		
		url = self.lineEdit.text()
		
		coub = Coub()
		if self.audioCheckBox.isChecked():
			coub.audio(url, addlink=True)
		
		if self.videoCheckBox.isChecked():
			coub.video(url, addlink=True)
		
		if self.previewCheckBox.isChecked():
			coub.lowvideo(url, addlink=False)
			self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "/tmp/tmp.mp4")))
			self.mediaPlayer.play()
		
		self.lineEdit.clear()
	
	def restart_program(self):
		"""
		Restarts the current program, with file objects and descriptors
		cleanup
		"""
		os.execl(sys.executable, *([sys.executable] + sys.argv))
	
	def audioCheckBox_toggle(self):
		"""
		changes the audiocheckbox setting based on whats checked
		"""
		if self.setting["audioCheckBox"] is False:
			self.setting["audioCheckBox"] = True
		
		elif self.setting["audioCheckBox"] is True:
			self.setting["audioCheckBox"] = False
		
		self.yaml_dump(self.setting)
	
	def videoCheckBox_toggle(self):
		"""
		changes the videocheckbox setting based on whats checked
		"""
		if self.setting["videoCheckBox"] is False:
			self.setting["videoCheckBox"] = True
		
		elif self.setting["videoCheckBox"] is True:
			self.setting["videoCheckBox"] = False
		
		self.yaml_dump(self.setting)
	
	def previewCheckBox_toggle(self):
		"""
		changes the previewCheckBox setting based on whats checked
		"""
		if self.setting["previewCheckBox"] is False:
			self.setting["previewCheckBox"] = True
		
		elif self.setting["previewCheckBox"] is True:
			self.setting["previewCheckBox"] = False
		
		self.yaml_dump(self.setting)
	
	def yaml_load(self):
		"""loads the yml config"""
		with open('recurces/setting.yaml', "r") as stream:
			setting = yaml.full_load(stream)
		return setting
	
	def yaml_dump(self, data):
		"""dumps to the yml config"""
		print(self.setting)
		with open('recurces/setting.yaml', 'w') as stream:
			yaml.dump(data, stream)


app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication

app.setStyle("Fusion")  # adding some style that makes more things dark
them = Theme()
app.setPalette(them.dark())  # adding the dark theme thats currently in that file, it can be modified to anything

window = Ui()  # Create an instance of our class
app.exec_()  # Start the application
