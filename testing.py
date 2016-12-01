#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pygame
#from PyQt5 import QApplication, QtWidgets
#from PyQt5.QtWidgets import (QWidget, QToolTip, 
#    QPushButton, QApplication, QMessageBox, QLabel,
#	QTextEdit, QGridLayout, QHBoxLayout, QVBoxLayout)
#from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
#                          QThreadPool, pyqtSignal)
#from PyQt5.QtGui import QFont    

# class ImageWidget(QtGui.QWidget):
	# def __init__(self, surface, parent=None):
		# super(ImageWidget,self).__init__(parent)
		# w = surface.get_width()
		# h = surface.get_height()
		# self.data = surface.get_buffer().raw
		# self.image = QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)
	
	# def paintEvent(self,event):
		# qp = QtGui.QPainter()
		# qp.begin(self)
		# qp.drawImage(0,0,self.image)
		# qp.end()

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.runningText = ''
	def initUI(self):
		
		self.sendLabel = QLabel('Send')
		self.sendLabel.setAlignment(Qt.AlignCenter)
		self.receiveLabel = QLabel('Receive')
		self.receiveLabel.setAlignment(Qt.AlignCenter)
		self.controlLabel = QLabel('Controls')
		self.controlLabel.setAlignment(Qt.AlignCenter)
		self.sendTextBox = QTextEdit()
		self.receiveTextBox = QTextEdit()
		self.mapWindow = QTextEdit()
		
		self.leftButton = QPushButton('Left', self)
		self.rightButton = QPushButton('Right', self)
		self.forwardButton = QPushButton('Forward', self)
		self.reverseButton = QPushButton('Reverse', self)
		self.stopButton = QPushButton('Stop', self)
		self.sendButton = QPushButton('Send', self)
		
		self.leftButton.clicked.connect(self.buttonClicked)
		self.rightButton.clicked.connect(self.buttonClicked)
		self.forwardButton.clicked.connect(self.buttonClicked)
		self.reverseButton.clicked.connect(self.buttonClicked)
		self.stopButton.clicked.connect(self.buttonClicked)
		self.sendButton.clicked.connect(self.buttonClicked)
		self.quitButton = QPushButton('Quit', self)
		self.quitButton.clicked.connect(QCoreApplication.instance().quit)
		#self.createGridLayout()
		
		#grid = QGridLayout()
		#grid.setSpacing(10)
		
		#grid.addWidget(sendLabel,0,0)
		#grid.addWidget(controlLabel,0,1)
		#grid.addWidget(receiveLabel,0,2)
		#grid.addWidget(sendTextBox,1,1,0,5)
		#grid.addWidget(receiveTextBox,2,1,0,5)
		#grid.addWidget(quitBtn,6,0,2,0)
		#self.setLayout(grid)
		
		
		self.vbox1 = QVBoxLayout()
		self.vbox1.addWidget(self.sendLabel)
		self.vbox1.addWidget(self.sendTextBox)
		#vbox1.setAlignment(Qt.AlignVCenter)
		
		#vbox1.addWidget(quitBtn)
		self.vbox2 = QVBoxLayout()
		#vbox2.addStretch()
		self.vbox2.addWidget(self.controlLabel)
		self.vbox2.addStretch()
		self.vbox2.addWidget(self.leftButton)
		self.vbox2.addWidget(self.rightButton)
		self.vbox2.addWidget(self.forwardButton)
		self.vbox2.addWidget(self.reverseButton)
		self.vbox2.addWidget(self.stopButton)
		self.vbox2.addStretch()
		
		self.vbox2.addWidget(self.sendButton)
		self.vbox2.addStretch()
		
		self.vbox3 = QVBoxLayout()
		self.vbox3.addWidget(self.receiveLabel)
		self.vbox3.addWidget(self.receiveTextBox)
		
		self.hbox1 = QHBoxLayout()
		self.hbox1.addLayout(self.vbox1)
		self.hbox1.addLayout(self.vbox2)
		self.hbox1.addLayout(self.vbox3)
		
		self.vboxMain = QVBoxLayout()
		self.vboxMain.addLayout(self.hbox1)
		self.vboxMain.addWidget(self.mapWindow)
		self.vboxMain.addWidget(self.quitButton)
		self.setLayout(self.vboxMain)
		self.setWindowTitle('Team 08 Python GUI')
		self.setGeometry(100,100,1200,800)
		self.show()
	
	#def createGridLayout(self):
		
	#def closeEvent(self, event):
	#	reply = QMessageBox.question(self, 'Message)
	
	# sample use of keyPressEvent, which closes window 
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()
	
	def buttonClicked(self):
		sender = self.sender()
		if sender.text() == 'Left':
			print('Left')
		elif sender.text() == 'Right':
			print('Right')
		elif sender.text() == 'Forward':
			print('Forward')
		elif sender.text() == 'Reverse':
			print('Reverse')
		elif sender.text() == 'Stop':
			print('Stop')
		elif sender.text() == 'Send':
			#print('Sending')
			myText = self.sendTextBox.toPlainText()
			self.runningText = self.runningText + myText + '\n'
			# we want to send it to the PIC32
			# for this testing we will just send from one box to another
			self.receiveTextBox.setText(self.runningText)
			self.sendTextBox.clear()
		else:
			print('Hello')
		
			
	
	
	


if __name__ == '__main__':
	pygame.init()
	app = QApplication(sys.argv)
	w = Window()
	sys.exit(app.exec_())