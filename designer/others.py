# -*- coding: utf-8 -*-

# From implementation generated from reading ui file 'Dni.ui'
#
# Created: Sat Apr 14 02:44:34 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(371, 217)
        Dialog.setMinimumSize(QtCore.QSize(371, 217))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 311, 151))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.entrada = QtGui.QLineEdit(self.layoutWidget)
        self.entrada.setObjectName(_fromUtf8("entrada"))
        self.horizontalLayout.addWidget(self.entrada)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.boton = QtGui.QPushButton(self.layoutWidget)
        self.boton.setObjectName(_fromUtf8("boton"))
        self.gridLayout.addWidget(self.boton, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.salida = QtGui.QLineEdit(self.layoutWidget)
        self.salida.setObjectName(_fromUtf8("salida"))
        self.horizontalLayout_2.addWidget(self.salida)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Introduzca su DNI", None, QtGui.QApplication.UnicodeUTF8))
        self.boton.setText(QtGui.QApplication.translate("Dialog", "Hallar NIF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "NIF:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
