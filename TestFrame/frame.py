#!/usr/bin/python3

from PyQt4 import QtCore, QtGui
#import RPi.GPIO as GPIO
import time
import threading

class ledThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        for i in range(30):
            GPIO.output(11,True)
            time.sleep(0.5)
            GPIO.output(11,False)
            time.sleep(0.5)
        window.runIconReset()
 


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        widget = QtGui.QWidget()
        self.setCentralWidget(widget)# bind widget to self.centralwidget

        topFiller = QtGui.QWidget()
        topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        self.infoLabel = QtGui.QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment=QtCore.Qt.AlignCenter)
        self.infoLabel.setFrameStyle(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)

        bottomFiller = QtGui.QWidget()
        bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)

        vbox = QtGui.QVBoxLayout()
        vbox.setMargin(5)
        vbox.addWidget(topFiller)
        vbox.addWidget(self.infoLabel)
        # vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)# centralWidget set layout

        self.createActions()
        self.createMenu()
        self.createToolBars()

        message = "A context menu is availabel by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("TestFrame")
        self.setMinimumSize(160, 160)
        self.resize(1024,768)
        self.setWindowIcon(QtGui.QIcon('images/strawberry_36X36.png'))

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())

    def undo(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def redo(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def about(self):
        self.infoLabel.setText("Invoked <b>Help|About</b>")
        QtGui.QMessageBox.about(self, "About Menu", 
                "The <b>TestFrame</b> runs HW test on RaspberryPi.<br/>"
                "With the annually upgrade of computing ability,<br/>"
                "Arm-Base Linux OS will be much usefull for human beings.<br/>"
                "Start from:2016-04-25")

    def aboutQt(self):
        self.infoLabel.setText("Invoked <b>Help|About Qt</b>")

    def runTest(self):
        self.runTestAct.setIcon(QtGui.QIcon('images/running.png'))
        self.infoLabel.setText("Invoked <b>Test|Run</b>")
        self.thread1 = ledThread()
        self.thread1.start()

    def stopTest(self):
        self.thread1.stop()
       #GPIO.cleanup()

    def runIconReset(self):
        self.runTestAct.setIcon(QtGui.QIcon('images/run.png'))

    def createActions(self):
        #----------Test menu-------------
        self.runTestAct = QtGui.QAction("&RunTest", self,
                shortcut="Alt+R",
                statusTip="Run test", triggered=self.runTest,
                icon=QtGui.QIcon('images/run.png'))

        self.stopTestAct = QtGui.QAction("&StopTest", self,
                shortcut="Alt+S",
                statusTip="Stop test", triggered= self.stopTest,
                icon=QtGui.QIcon('images/stop.png'))

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        #-----------Edit menu-----------
        self.undoAct = QtGui.QAction("&Undo", self,
                shortcut=QtGui.QKeySequence.Undo,
                statusTip="Undo the last operation", triggered=self.undo,
                icon=QtGui.QIcon('images/undo.png'))
        
        self.redoAct = QtGui.QAction("&Redo", self,
                shortcut=QtGui.QKeySequence.Redo,
                statusTip="Redo the last operation", triggered=self.redo,
                icon=QtGui.QIcon('images/redo.png'))

        self.cutAct = QtGui.QAction("Cu&t", self,
                shortcut=QtGui.QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.cut,
                icon=QtGui.QIcon('images/cut.png'))

        self.copyAct = QtGui.QAction("&Copy", self,
                shortcut=QtGui.QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.copy,
                icon=QtGui.QIcon('images/copy.png'))

        self.pasteAct = QtGui.QAction("&Paste", self,
                shortcut=QtGui.QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.paste,
                icon=QtGui.QIcon('images/paste.png'))

        #-----------Help menu------------
        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=self.aboutQt)
        self.aboutQtAct.triggered.connect(QtGui.qApp.aboutQt)

    def createMenu(self):
        self.fileMenu = self.menuBar().addMenu("&Test")
        self.fileMenu.addAction(self.runTestAct)
        self.fileMenu.addAction(self.stopTestAct)
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        self.testToolBar = self.addToolBar("Test")
        self.testToolBar.addAction(self.runTestAct)
        self.testToolBar.addAction(self.stopTestAct)
        self.testToolBar.setMovable(False)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
