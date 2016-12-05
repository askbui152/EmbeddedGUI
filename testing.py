#!/usr/bin/python3

import sys
import time
import threading
import asyncore
import socket
import time
#import syslog
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



class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.runningText = ''
		self.runningText2 = ''
	def initUI(self):
		#os.system('testing2.py')
		self.TCP_IP = '192.168.10.107'
		self.TCP_PORT = 2000
		self.size = 1024
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.TCP_IP,int(self.TCP_PORT)))
		#self.data = self.s.recv(208192)
		#self.receiveTextBox.setText('hello')
		# self.appendTextBox()
		self.sendLabel = QLabel('Send')
		self.sendLabel.setAlignment(Qt.AlignCenter)
		self.receiveLabel = QLabel('Receive')
		self.receiveLabel.setAlignment(Qt.AlignCenter)
		self.controlLabel = QLabel('Controls')
		self.controlLabel.setAlignment(Qt.AlignCenter)
		self.sendTextBox = QTextEdit()
		self.receiveTextBox = QTextEdit()
		self.mapWindow = QTextEdit()
		
		self.autoButton = QPushButton('Auto', self)
		self.leftButton = QPushButton('Left', self)
		self.rightButton = QPushButton('Right', self)
		self.forwardButton = QPushButton('Forward', self)
		self.reverseButton = QPushButton('Reverse', self)
		self.stopButton = QPushButton('Stop', self)
		self.sendButton = QPushButton('Send', self)
		self.receiveButton = QPushButton('Receive', self)
		
		self.autoButton.clicked.connect(self.buttonClicked)
		self.leftButton.clicked.connect(self.buttonClicked)
		self.rightButton.clicked.connect(self.buttonClicked)
		self.forwardButton.clicked.connect(self.buttonClicked)
		self.reverseButton.clicked.connect(self.buttonClicked)
		self.stopButton.clicked.connect(self.buttonClicked)
		self.sendButton.clicked.connect(self.buttonClicked)
		self.receiveButton.clicked.connect(self.buttonClicked)
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
		self.vbox2.addWidget(self.autoButton)
		self.vbox2.addStretch()
		self.vbox2.addWidget(self.leftButton)
		self.vbox2.addWidget(self.rightButton)
		self.vbox2.addWidget(self.forwardButton)
		self.vbox2.addWidget(self.reverseButton)
		self.vbox2.addWidget(self.stopButton)
		self.vbox2.addWidget(self.receiveButton)
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
		
		self.vboxMain.addWidget(self.quitButton)
		
		
		self.setLayout(self.vboxMain)
		self.setWindowTitle('Team 08 Python GUI')
		self.setGeometry(100,100,800,600)
		self.show()
	
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.s.close()
			self.close()
	
	def appendTextBox(self):
		#self.runningText = self.runningText + self.data + '\n'
		self.data = self.s.recv(208192)
		self.runningText = self.runningText + str(self.data) + '\n'
		self.receiveTextBox.setText(self.runningText)
	def turnLeft(self):
		self.s.send(b'R')
		sendDir2 = 'Left'
		sendDir = 'Left-Ack'
		self.runningText = self.runningText + sendDir + '\n'
		self.runningText2 = self.runningText2 + sendDir2 + '\n'
		self.sendTextBox.setText(self.runningText2)
		#time.sleep(1)
		self.receiveTextBox.setText(self.runningText)
		print('Left')
	
	def turnRight(self):
		self.s.send(b'L')
		sendDir2 = 'Right'
		sendDir = 'Right-Ack'
		self.runningText = self.runningText + sendDir + '\n'
		self.runningText2 = self.runningText2 + sendDir2 + '\n'
		self.sendTextBox.setText(self.runningText2)
		#time.sleep(1)
		self.receiveTextBox.setText(self.runningText)
		print('Right')
	
	def turnForward(self):
		self.s.send(b'F')
		sendDir2 = 'Forward'
		sendDir = 'Forward-Ack'
		self.runningText = self.runningText + sendDir + '\n'
		self.runningText2 = self.runningText2 + sendDir2 + '\n'
		self.sendTextBox.setText(self.runningText2)
		#time.sleep(1)
		self.receiveTextBox.setText(self.runningText)
		print('Forward')
	
	def turnReverse(self):
		self.s.send(b'B')
		sendDir2 = 'Reverse'
		sendDir = 'Reverse-Ack'
		self.runningText = self.runningText + sendDir + '\n'
		self.runningText2 = self.runningText2 + sendDir2 + '\n'
		self.sendTextBox.setText(self.runningText2)
		#time.sleep(1)
		self.receiveTextBox.setText(self.runningText)
		print('Reverse')
	
	def turnStop(self):
		self.s.send(b'S')
		sendDir2 = 'Stop'
		sendDir = 'Stop-Ack'
		self.runningText = self.runningText + sendDir + '\n'
		self.runningText2 = self.runningText2 + sendDir2 + '\n'
		self.sendTextBox.setText(self.runningText2)
		#time.sleep(1)
		self.receiveTextBox.setText(self.runningText)
		print('Stop')
	
	def buttonClicked(self):
		sender = self.sender()
		if sender.text() == 'Auto':
			sendAuto2 = 'Auto'
			sendAuto = 'Auto-Ack'
			self.runningText = self.runningText + sendAuto + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			#time.sleep(1)
			self.receiveTextBox.setText(self.runningText)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			
			# first check left right
			self.turnLeft()
			time.sleep(2)
			# first car
			sendAuto2 = 'Check distance'
			sendAuto = 'IR: Object detected'
			sendAuto3 = 'IR: No object detected'
			self.runningText = self.runningText + sendAuto + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnRight()
			time.sleep(2)
			self.turnRight()
			time.sleep(2)
			# second car
			self.runningText = self.runningText + sendAuto + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnLeft()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			
			# second check left right
			self.turnLeft()
			time.sleep(2)
			# third car
			self.runningText = self.runningText + sendAuto + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnRight()
			time.sleep(2)
			self.turnRight()
			time.sleep(2)
			self.runningText = self.runningText + sendAuto3 + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnLeft()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			
			# third check left right
			self.turnLeft()
			time.sleep(2)
			self.runningText = self.runningText + sendAuto3 + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnRight()
			time.sleep(2)
			self.turnRight()
			time.sleep(2)
			self.runningText = self.runningText + sendAuto3 + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnLeft()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			time.sleep(2)
			self.turnForward()
			
			# fourth check left right 
			self.turnLeft()
			time.sleep(2)
			self.runningText = self.runningText + sendAuto + '\n'
			self.runningText2 = self.runningText2 + sendAuto2 + '\n'
			self.sendTextBox.setText(self.runningText2)
			self.receiveTextBox.setText(self.runningText)
			self.turnRight()
			time.sleep(2)
			self.turnRight()
			time.sleep(2)
			self.turnLeft()

		elif sender.text() == 'Left':
			self.turnLeft()
		elif sender.text() == 'Right':
			self.turnRight()
		elif sender.text() == 'Forward':
			self.turnForward()
		elif sender.text() == 'Reverse':
			self.turnReverse()
		elif sender.text() == 'Stop':
			self.turnStop()
		elif sender.text() == 'Send':
			myText = self.sendTextBox.toPlainText()
			self.runningText = self.runningText + myText + '\n'
			# we want to send it to the PIC32
			# for this testing we will just send from one box to another
			self.receiveTextBox.setText(self.runningText)
			self.sendTextBox.clear()
		elif sender.text() == 'Receive':
			self.appendTextBox()
		else:
			print('Hello')
		

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        startBool
        #data = self.recv(8192)
        data = self.recv(208192)
		
        #print(data)
        log_and_interpret_data(data)
        sendAll('K')
        #interpretData(data)
        #if data:
            #self.send(data)
            #sendAll(data)
			
class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)

        self.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        to = convert_symbol(data[1])
        _from = convert_symbol(data[2])
        data = data.replace('~','')
        data = data.replace('*','')
        log_entry = "Communication from " + _from + " to " + to  + " Data: "  + data
        print(log_entry)
#write_to_syslog(log_entry)
    #else:
        if(data[0] != '~' ):
            print('Did not receive start bit:  '  + data)
            #write_to_syslog("Did not receive start bit " + data)
        elif (data[11] != '*'):
            print ('Did not receive end bit  '  + data)
           # write_to_syslog("Did not receive end bit " + data)
        elif(len(data) != 12):
            print ('Message is not the correct size  ' + data)
            #write_to_syslog("Message is not the correct size " + data)
        else:
            print ('Corrupt Data')
            #write_to_syslog("Corrupted Data" + data)
class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        #.create_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.create_socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        print ('I am listening...')

	#self.set_reuse_addr()
        self.s.bind((host, port))
        self.s.listen(1)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            conns.append(sock)
            print ('Incoming connection from %s') % repr(addr)
            handler = EchoHandler(sock)	
	
	


if __name__ == '__main__':
	#Open up Syslog
	#syslog.openlog(ident = 'Team08',logoption = syslog.LOG_NDELAY,facility = syslog.LOG_LOCAL0)
	conns = []
	myData = " "
	startBool = False
	app = QApplication(sys.argv)
	w = Window()
	#server = EchoServer('', 57600)
	#asyncore.loop()
	#w = Window()
	#b = Board()
	sys.exit(app.exec_())