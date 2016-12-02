#!/usr/bin/python3

import sys
import time
import threading
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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

class Board(QWidget):

	boardWidth = 20;
	boardHeight = 20;
	def __init__(self):
		super().__init__()
		self.map = [[0 for i in range(20)] for i in range(20)]
		#for i in range(20):
		#	for j in range(20):
		#		print(self.map[i][j])
		self.initUI()
	
	def initUI(self):
		#self.setStyleSheet("QWidget { background: #A9F5D0 }")
		self.setStyleSheet("QWidget { background: #FFFFFF }")
		self.newStart()
		#self.setFixedSize(500,500)
		self.createMap()
		self.resize(200,200)
		self.setWindowTitle('Board')
		self.show()
		
		
		#self.map = [[10,10], [20,10], [30,10], [40,10], [50,10]
		#            [60,10], [70,10], [80,10],[90,10]]
		#print(self.map)
	def paintEvent(self, e):
		painter = QPainter()
		painter.begin(self)
		self.drawMap(painter)
		self.drawCar(painter)
		painter.end()
		
	def keyPressEvent(self,e):
		key = e.key()
		if key == Qt.Key_Left:
			self.direction('LEFT')
			#print('LEFT')
		elif key == Qt.Key_Right:
			self.direction('RIGHT')
		elif key == Qt.Key_Up:
			self.direction('UP')
		elif key == Qt.Key_Down:
			self.direction('DOWN')
		elif key == Qt.Key_Escape:
			self.close()
	
	def newStart(self):
		self.x = 20;
		self.y = 20;
		self.prevX = 0;
		self.prevY = 0;
		self.carPos = [self.x, self.y]
		self.carPrevPos = [self.prevX, self.prevY]
	
	def direction(self, dir):
		self.prevX = self.x
		self.prevY = self.y
		if dir == 'DOWN':
			#if self.map[int(self.x/10)][int(self.y/10)] == 1:
			if self.map[int((self.y+10)/10)][int(self.x/10)] == 1:
				self.y = self.y + 10
			else:
				self.y = self.y
		elif dir == 'UP':
			#if self.map[int(self.x/10)][int(self.y/10)] == 1:
			if self.map[int((self.y-10)/10)][int(self.x/10)] == 1:
				self.y = self.y - 10
			else:
				self.y = self.y
		elif dir == 'RIGHT':
			if self.map[int(self.y/10)][int((self.x+10)/10)] == 1:
				self.x = self.x + 10
			else:
				self.x = self.x
		elif dir == 'LEFT':
			if self.map[int(self.y/10)][int((self.x-10)/10)] == 1:
				self.x = self.x - 10
			else:
				self.x = self.x
		print("X: {}   Y: {}  ".format(self.x/10, self.y/10))
		print
		self.repaint()
		self.carPos = [self.x, self.y]
		self.carPrevPos = [self.prevX, self.prevY]
	
	def createMap(self):
		# top horizontal
		for i in range(2,17):
			self.map[2][i] = 1
		
		# right vertical
		for i in range(2,8):
			self.map[i][17] = 1
		
		# second horizontal
		for i in range(2,17):
			self.map[7][i] = 1
		
		# left vertical
		for i in range(7,12):
			self.map[i][2] = 1
		
		# third horizontal
		for i in range(2, 17):
			self.map[12][i] = 1
		
		# right vertical
		for i in range(12,20):
			self.map[i][17] = 1
			
	def drawMap(self, painter):
		blackColor = QColor(0x000000)
		whiteColor = QColor(0xFFFFFF)
		brush = QBrush(Qt.SolidPattern)
		#brush.setColor(blackColor)
		#painter.setBrush(brush)
		for i in range(20):
			for j in range(20):
				if self.map[i][j] == 1:
					brush.setColor(blackColor)
					painter.setBrush(brush)
					painter.drawRect(j * 10, i * 10, 10, 10)
				#if self.map[i][j] == 0:
				#	brush.setColor(whiteColor)
				#	painter.setBrush(brush)
				#	painter.drawRect(i * 10, j * 10, 10, 10)
				#else:
				#	brush.setColor(blackColor)
				#	painter.setBrush(brush)
				#	painter.drawRect(i * 10, j * 10, 10, 10)
				
		
	def drawCar(self, painter):
		blueColor = QColor(0x66CCCC)
		whiteColor = QColor(0xFFFFFF)
		
		brush = QBrush(Qt.SolidPattern)
		brush.setColor(blueColor)
		painter.setBrush(brush)
		painter.drawRect(self.x, self.y, 10,10)
		
		#brush.setColor(whiteColor)
		#painter.setBrush(brush)
		#painter.drawRect(self.prevX, self.prevY, 12,12)
		#painter.drawRect(self.x, self.y, 1, 1, color)
		
		
		
			
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
		self.boardWindow = Board()
		
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
		self.vboxMain.addStretch()
		self.vboxMain.addWidget(self.boardWindow)
		self.vboxMain.addStretch()
		#self.vboxMain.addWidget(self.mapWindow)
		
		self.vboxMain.addWidget(self.quitButton)
		self.setLayout(self.vboxMain)
		self.setWindowTitle('Team 08 Python GUI')
		self.setGeometry(100,100,800,600)
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
		
# class Board(QFrame):
	# boardWidth = 10
	# boardHeight = 22
	# Speed = 300
	
	# def __init__(self,parent):
		# super().__init__(parent)
		# #self.initBoard()
	
	# #def initBoard(self):
		
	
	
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	#w = Window()
	b = Board()
	sys.exit(app.exec_())