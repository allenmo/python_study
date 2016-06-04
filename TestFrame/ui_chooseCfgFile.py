# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooseCfgFile.ui'
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

class Ui_DialogChooseCfgFile(object):
    def setupUi(self, DialogChooseCfgFile):
        DialogChooseCfgFile.setObjectName(_fromUtf8("DialogChooseCfgFile"))
        DialogChooseCfgFile.setWindowModality(QtCore.Qt.NonModal)
        DialogChooseCfgFile.resize(300, 268)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogChooseCfgFile.sizePolicy().hasHeightForWidth())
        DialogChooseCfgFile.setSizePolicy(sizePolicy)
        DialogChooseCfgFile.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(DialogChooseCfgFile)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DialogChooseCfgFile)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listWidgetModel = QtGui.QListWidget(DialogChooseCfgFile)
        self.listWidgetModel.setObjectName(_fromUtf8("listWidgetModel"))
        self.verticalLayout.addWidget(self.listWidgetModel)
        self.buttonBox = QtGui.QDialogButtonBox(DialogChooseCfgFile)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.listWidgetModel)

        self.retranslateUi(DialogChooseCfgFile)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogChooseCfgFile.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogChooseCfgFile.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogChooseCfgFile)

    def retranslateUi(self, DialogChooseCfgFile):
        DialogChooseCfgFile.setWindowTitle(_translate("DialogChooseCfgFile", "Dialog", None))
        self.label.setText(_translate("DialogChooseCfgFile", "Please choose Model:", None))

