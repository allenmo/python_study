#!/usr/bin/python3

import sys, time
from PyQt4 import QtCore, QtGui 
class Logger(QtGui.QWidget):
	def __init__(self, *args):
		QtGui.QWidget.__init__(self, *args)
		# self.setCaption("Timestamp logging application")
		self.layout = QtGui.QGridLayout(self)
		self.tsdisp = QtGui.QTextEdit(self)
		self.tsdisp.setMinimumSize(250, 300)
		# self.tsdisp.setTextFormat(Qt.PlainText)
		self.tscount = QtGui.QLabel("", self)
		# self.tscount.setFont(QFont("Sans", 24))
		self.log = QtGui.QPushButton("&Log Timestamp", self)
		self.quit = QtGui.QPushButton("&Quit", self)
		# self.layout.addMultiCellWidget(self.tsdisp, 0, 2, 0, 0)
		self.layout.addWidget(self.tscount, 0, 1)
		self.layout.addWidget(self.log, 1, 1)
		self.layout.addWidget(self.quit, 2, 1)
		self.connect(self.log, QtCore.SIGNAL("clicked()"), self.log_timestamp)
		self.connect(self.quit, QtCore.SIGNAL("clicked()"), self.close)

	def log_timestamp(self):
		stamp = time.ctime()
		self.tsdisp.append(stamp)
		self.tscount.setText(str(self.tsdisp.lines()))
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.connect(app, QtCore.SIGNAL('lastWindowClosed()'), QtCore.SLOT('quit()'))
	logger = Logger()
	logger.show()
	# app.setMainWidget(logger)
	# app.exec_loop()
	# sys.exit(logger.exec_())
