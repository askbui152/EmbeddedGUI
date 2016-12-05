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
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.host = socket.gethostname()
		self.port = 9000
		self.s.bind((self.host,self.port))
		self.s.listen(1)
		
		#self.setStyleSheet("QWidget { background: #A9F5D0 }")
		self.setStyleSheet("QWidget { background: #FFFFFF }")
		self.newStart()
		#self.setFixedSize(500,500)
		#self.createMap()
		self.createMap2()
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
		self.x = 10;
		self.y = 100;
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
			
	
	def createMap2(self):
		# road
		for i in range(1, 18):
			self.map[10][i] = 1
		
		# parking spots
		for i in range(9,12):
			self.map[i][3] = 1
		
		for i in range(9,12):
			self.map[i][6] = 1
		
		for i in range(9,12):
			self.map[i][9] = 1
			
		for i in range(9,12):
			self.map[i][12] = 1
		
		for i in range(9,12):
			self.map[i][15] = 1
		
		
			
			
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
	#conns = []
	#myData = " "
	#startBool = False
	app = QApplication(sys.argv)
	#w = Window()
	#server = EchoServer('', 57600)
	#asyncore.loop()
	#w = Window()
	b = Board()
	sys.exit(app.exec_())