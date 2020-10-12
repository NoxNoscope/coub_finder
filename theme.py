# this code is from this dude https://github.com/steam3d/coub-dl
# i have no clue how to do this corectly so idk.py here ya go
import requests, urllib.request, json
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Theme:
	def __init__(self):
		print("ah")
		
	def dark(self):
		palette = QPalette()
		palette.setColor(QPalette.Window, QColor(53, 53, 53))
		palette.setColor(QPalette.WindowText, Qt.white)
		palette.setColor(QPalette.Base, QColor(25, 25, 25))
		palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		palette.setColor(QPalette.ToolTipBase, Qt.black)
		palette.setColor(QPalette.ToolTipText, Qt.white)
		palette.setColor(QPalette.Text, Qt.white)
		palette.setColor(QPalette.Button, Qt.black)
		palette.setColor(QPalette.ButtonText, Qt.white)
		palette.setColor(QPalette.BrightText, Qt.red)
		palette.setColor(QPalette.Link, QColor(42, 130, 218))
		palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
		palette.setColor(QPalette.HighlightedText, Qt.black)
		return palette


	def flashbang(self):
		palette = QPalette()

		return palette


if __name__ == "__main__":
	url = 'https://coub.com/view/iyd2d'
	theme = Theme()
