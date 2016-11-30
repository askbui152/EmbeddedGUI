#!/usr/bin/python3

import sys
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

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		
		sendLabel = QLabel('Send')
		sendLabel.setAlignment(Qt.AlignCenter)
		receiveLabel = QLabel('Receive')
		receiveLabel.setAlignment(Qt.AlignCenter)
		controlLabel = QLabel('Controls')
		controlLabel.setAlignment(Qt.AlignCenter)
		sendTextBox = QTextEdit()
		receiveTextBox = QTextEdit()
		
		leftButton = QPushButton('Left', self)
		rightButton = QPushButton('Right', self)
		forwardButton = QPushButton('Forward', self)
		reverseButton = QPushButton('Reverse', self)
		stopButton = QPushButton('Stop', self)
		
		quitButton = QPushButton('Quit', self)
		quitButton.clicked.connect(QCoreApplication.instance().quit)
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
		
		
		vbox1 = QVBoxLayout()
		vbox1.addWidget(sendLabel)
		vbox1.addWidget(sendTextBox)
		#vbox1.setAlignment(Qt.AlignVCenter)
		
		#vbox1.addWidget(quitBtn)
		vbox2 = QVBoxLayout()
		#vbox2.addStretch()
		vbox2.addWidget(controlLabel)
		vbox2.addStretch()
		vbox2.addWidget(leftButton)
		vbox2.addWidget(rightButton)
		vbox2.addWidget(forwardButton)
		vbox2.addWidget(reverseButton)
		vbox2.addWidget(stopButton)
		vbox2.addStretch()
		
		vbox3 = QVBoxLayout()
		vbox3.addWidget(receiveLabel)
		vbox3.addWidget(receiveTextBox)
		
		hbox1 = QHBoxLayout()
		hbox1.addLayout(vbox1)
		hbox1.addLayout(vbox2)
		hbox1.addLayout(vbox3)
		
		vboxMain = QVBoxLayout()
		vboxMain.addLayout(hbox1)
		vboxMain.addWidget(quitButton)
		self.setLayout(vboxMain)
		self.setWindowTitle('Team 08 Python GUI')
		self.setGeometry(600,600,600,300)
		self.show()
	
	#def createGridLayout(self):
		
	#def closeEvent(self, event):
	#	reply = QMessageBox.question(self, 'Message)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Window()
	sys.exit(app.exec_())