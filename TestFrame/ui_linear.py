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
        MainWindow.setMouseTracking(True)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.labelSoftwareNameVersion = QtGui.QLabel(self.centralwidget)
        self.labelSoftwareNameVersion.setGeometry(QtCore.QRect(330, 0, 351, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelSoftwareNameVersion.setFont(font)
        self.labelSoftwareNameVersion.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelSoftwareNameVersion.setObjectName(_fromUtf8("labelSoftwareNameVersion"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(150, 160, 85, 27))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(150, 190, 85, 27))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 32, 732, 99))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelCustomer = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCustomer.sizePolicy().hasHeightForWidth())
        self.labelCustomer.setSizePolicy(sizePolicy)
        self.labelCustomer.setMinimumSize(QtCore.QSize(0, 27))
        self.labelCustomer.setObjectName(_fromUtf8("labelCustomer"))
        self.verticalLayout.addWidget(self.labelCustomer)
        self.labelProdPN = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProdPN.sizePolicy().hasHeightForWidth())
        self.labelProdPN.setSizePolicy(sizePolicy)
        self.labelProdPN.setMinimumSize(QtCore.QSize(0, 27))
        self.labelProdPN.setObjectName(_fromUtf8("labelProdPN"))
        self.verticalLayout.addWidget(self.labelProdPN)
        self.labelSN = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSN.sizePolicy().hasHeightForWidth())
        self.labelSN.setSizePolicy(sizePolicy)
        self.labelSN.setMinimumSize(QtCore.QSize(0, 27))
        self.labelSN.setObjectName(_fromUtf8("labelSN"))
        self.verticalLayout.addWidget(self.labelSN)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lineEditCustomer = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCustomer.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCustomer.sizePolicy().hasHeightForWidth())
        self.lineEditCustomer.setSizePolicy(sizePolicy)
        self.lineEditCustomer.setMouseTracking(False)
        self.lineEditCustomer.setObjectName(_fromUtf8("lineEditCustomer"))
        self.verticalLayout_6.addWidget(self.lineEditCustomer)
        self.lineEditProdPN = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditProdPN.setEnabled(False)
        self.lineEditProdPN.setText(_fromUtf8(""))
        self.lineEditProdPN.setPlaceholderText(_fromUtf8(""))
        self.lineEditProdPN.setObjectName(_fromUtf8("lineEditProdPN"))
        self.verticalLayout_6.addWidget(self.lineEditProdPN)
        self.lineEditSN = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSN.setEnabled(False)
        self.lineEditSN.setText(_fromUtf8(""))
        self.lineEditSN.setPlaceholderText(_fromUtf8(""))
        self.lineEditSN.setObjectName(_fromUtf8("lineEditSN"))
        self.verticalLayout_6.addWidget(self.lineEditSN)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelStation = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStation.sizePolicy().hasHeightForWidth())
        self.labelStation.setSizePolicy(sizePolicy)
        self.labelStation.setMinimumSize(QtCore.QSize(0, 27))
        self.labelStation.setObjectName(_fromUtf8("labelStation"))
        self.verticalLayout_2.addWidget(self.labelStation)
        self.labelFixtureSN = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFixtureSN.sizePolicy().hasHeightForWidth())
        self.labelFixtureSN.setSizePolicy(sizePolicy)
        self.labelFixtureSN.setMinimumSize(QtCore.QSize(0, 27))
        self.labelFixtureSN.setObjectName(_fromUtf8("labelFixtureSN"))
        self.verticalLayout_2.addWidget(self.labelFixtureSN)
        self.labelComputerID = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComputerID.sizePolicy().hasHeightForWidth())
        self.labelComputerID.setSizePolicy(sizePolicy)
        self.labelComputerID.setMinimumSize(QtCore.QSize(0, 27))
        self.labelComputerID.setObjectName(_fromUtf8("labelComputerID"))
        self.verticalLayout_2.addWidget(self.labelComputerID)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lineEditStation = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditStation.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditStation.sizePolicy().hasHeightForWidth())
        self.lineEditStation.setSizePolicy(sizePolicy)
        self.lineEditStation.setMouseTracking(False)
        self.lineEditStation.setObjectName(_fromUtf8("lineEditStation"))
        self.verticalLayout_5.addWidget(self.lineEditStation)
        self.lineEditFixtureSN = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditFixtureSN.setEnabled(False)
        self.lineEditFixtureSN.setText(_fromUtf8(""))
        self.lineEditFixtureSN.setPlaceholderText(_fromUtf8(""))
        self.lineEditFixtureSN.setObjectName(_fromUtf8("lineEditFixtureSN"))
        self.verticalLayout_5.addWidget(self.lineEditFixtureSN)
        self.lineEditComputerID = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditComputerID.setEnabled(False)
        self.lineEditComputerID.setText(_fromUtf8(""))
        self.lineEditComputerID.setPlaceholderText(_fromUtf8(""))
        self.lineEditComputerID.setObjectName(_fromUtf8("lineEditComputerID"))
        self.verticalLayout_5.addWidget(self.lineEditComputerID)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelOperator = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOperator.sizePolicy().hasHeightForWidth())
        self.labelOperator.setSizePolicy(sizePolicy)
        self.labelOperator.setMinimumSize(QtCore.QSize(0, 27))
        self.labelOperator.setObjectName(_fromUtf8("labelOperator"))
        self.verticalLayout_3.addWidget(self.labelOperator)
        self.labelErrorCode = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelErrorCode.sizePolicy().hasHeightForWidth())
        self.labelErrorCode.setSizePolicy(sizePolicy)
        self.labelErrorCode.setMinimumSize(QtCore.QSize(0, 27))
        self.labelErrorCode.setObjectName(_fromUtf8("labelErrorCode"))
        self.verticalLayout_3.addWidget(self.labelErrorCode)
        self.labelErrorMsg = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelErrorMsg.sizePolicy().hasHeightForWidth())
        self.labelErrorMsg.setSizePolicy(sizePolicy)
        self.labelErrorMsg.setMinimumSize(QtCore.QSize(0, 27))
        self.labelErrorMsg.setObjectName(_fromUtf8("labelErrorMsg"))
        self.verticalLayout_3.addWidget(self.labelErrorMsg)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEditOperator = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditOperator.setEnabled(False)
        self.lineEditOperator.setText(_fromUtf8(""))
        self.lineEditOperator.setPlaceholderText(_fromUtf8(""))
        self.lineEditOperator.setObjectName(_fromUtf8("lineEditOperator"))
        self.verticalLayout_4.addWidget(self.lineEditOperator)
        self.lineEditErrorCode = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditErrorCode.setEnabled(False)
        self.lineEditErrorCode.setText(_fromUtf8(""))
        self.lineEditErrorCode.setPlaceholderText(_fromUtf8(""))
        self.lineEditErrorCode.setObjectName(_fromUtf8("lineEditErrorCode"))
        self.verticalLayout_4.addWidget(self.lineEditErrorCode)
        self.lineEditErrorMsg = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditErrorMsg.setEnabled(False)
        self.lineEditErrorMsg.setText(_fromUtf8(""))
        self.lineEditErrorMsg.setPlaceholderText(_fromUtf8(""))
        self.lineEditErrorMsg.setObjectName(_fromUtf8("lineEditErrorMsg"))
        self.verticalLayout_4.addWidget(self.lineEditErrorMsg)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.textEditMsg = QtGui.QTextEdit(self.centralwidget)
        self.textEditMsg.setGeometry(QtCore.QRect(760, 60, 251, 651))
        self.textEditMsg.setObjectName(_fromUtf8("textEditMsg"))
        self.labelMessage = QtGui.QLabel(self.centralwidget)
        self.labelMessage.setGeometry(QtCore.QRect(760, 40, 64, 17))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
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
        self.labelCustomer.setBuddy(self.lineEditCustomer)
        self.labelProdPN.setBuddy(self.lineEditProdPN)
        self.labelSN.setBuddy(self.lineEditSN)
        self.labelStation.setBuddy(self.lineEditStation)
        self.labelFixtureSN.setBuddy(self.lineEditFixtureSN)
        self.labelComputerID.setBuddy(self.lineEditComputerID)
        self.labelOperator.setBuddy(self.lineEditOperator)
        self.labelErrorCode.setBuddy(self.lineEditErrorCode)
        self.labelErrorMsg.setBuddy(self.lineEditErrorMsg)
        self.labelMessage.setBuddy(self.textEditMsg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelSoftwareNameVersion.setText(_translate("MainWindow", "TestProgramName(Version)", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.labelCustomer.setText(_translate("MainWindow", "Customer:", None))
        self.labelProdPN.setText(_translate("MainWindow", "Product PN:", None))
        self.labelSN.setText(_translate("MainWindow", "SN:", None))
        self.labelStation.setText(_translate("MainWindow", "Station:", None))
        self.labelFixtureSN.setText(_translate("MainWindow", "FixtureSN:", None))
        self.labelComputerID.setText(_translate("MainWindow", "ComputerID:", None))
        self.labelOperator.setText(_translate("MainWindow", "Operator:", None))
        self.labelErrorCode.setText(_translate("MainWindow", "ErrorCode:", None))
        self.labelErrorMsg.setText(_translate("MainWindow", "ErrorMsg:", None))
        self.textEditMsg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.labelMessage.setText(_translate("MainWindow", "Message:", None))
        self.menuTest.setTitle(_translate("MainWindow", "&Test", None))
        self.menuCon_fig.setTitle(_translate("MainWindow", "Con&figure", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_Start_Test.setText(_translate("MainWindow", "&Load Test", None))
        self.actionSt_op_Test.setText(_translate("MainWindow", "&Run  Test", None))
        self.action_Stop_Test.setText(_translate("MainWindow", "&Stop Test", None))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit", None))
        self.action_Port.setText(_translate("MainWindow", "&Equipment", None))
        self.actionSte_p.setText(_translate("MainWindow", "Ste&p", None))

