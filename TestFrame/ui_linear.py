# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_linear.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 351, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.okButton = QtGui.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(460, 270, 99, 27))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(610, 270, 99, 27))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        self.menuCon_fig = QtGui.QMenu(self.menubar)
        self.menuCon_fig.setObjectName(_fromUtf8("menuCon_fig"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Start_Test = QtGui.QAction(MainWindow)
        self.action_Start_Test.setObjectName(_fromUtf8("action_Start_Test"))
        self.actionSt_op_Test = QtGui.QAction(MainWindow)
        self.actionSt_op_Test.setObjectName(_fromUtf8("actionSt_op_Test"))
        self.action_Stop_Test = QtGui.QAction(MainWindow)
        self.action_Stop_Test.setObjectName(_fromUtf8("action_Stop_Test"))
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName(_fromUtf8("actionE_xit"))
        self.action_Port = QtGui.QAction(MainWindow)
        self.action_Port.setObjectName(_fromUtf8("action_Port"))
        self.actionSte_p = QtGui.QAction(MainWindow)
        self.actionSte_p.setObjectName(_fromUtf8("actionSte_p"))
        self.menuTest.addAction(self.action_Start_Test)
        self.menuTest.addAction(self.actionSt_op_Test)
        self.menuTest.addAction(self.action_Stop_Test)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionE_xit)
        self.menuCon_fig.addAction(self.action_Port)
        self.menuCon_fig.addAction(self.actionSte_p)
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuCon_fig.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "TestProgramName(Version)", None))
        self.okButton.setText(_translate("MainWindow", "OK", None))
        self.cancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.menuTest.setTitle(_translate("MainWindow", "&Test", None))
        self.menuCon_fig.setTitle(_translate("MainWindow", "Con&figure", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_Start_Test.setText(_translate("MainWindow", "&Load Test", None))
        self.actionSt_op_Test.setText(_translate("MainWindow", "&Run  Test", None))
        self.action_Stop_Test.setText(_translate("MainWindow", "&Stop Test", None))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit", None))
        self.action_Port.setText(_translate("MainWindow", "&Equipment", None))
        self.actionSte_p.setText(_translate("MainWindow", "Ste&p", None))

