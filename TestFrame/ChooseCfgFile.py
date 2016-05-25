# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui_chooseCfgFile import Ui_DialogChooseCfgFile

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

class ChooseCfgFile(Ui_DialogChooseCfgFile):
    def readLvFile(self, DialogChooseCfgFile):
        import os
        LvFile = "Lv.ini"
        if os.path.isfile(LvFile):
            with open(LvFile, "r") as f:
                kvs = f.readlines()
                for idx, line in enumerate(kvs):
                    kv = line.split(",")
                    #print("len(kv)=%d"%len(kv))
                    if len(kv) ==2:
                        item = QtGui.QListWidgetItem()
                        self.listWidgetModel.addItem(item)
                        addedItem = self.listWidgetModel.item(idx)
                        #print("type(itme):%s"%type(item))
                        addedItem.setText(_translate("DialogChooseCfgFile", kv[0], None))

#    def accept(self)
#        print("in my accept()")
#        self.accept(self)
   
    @staticmethod
    def getModel(parentDlg):
        dialog = QtGui.QDialog(parent=parentDlg, modal=True)
        dialogChoose = ChooseCfgFile()
        dialogChoose.setupUi(dialog)
        #dialog.setSizeGripEnabled(True)
        #dialog.show() # none modal type show the window
        #print("isSizeGripEnabled:%s"%dialog.isSizeGripEnabled())
        dialogChoose.readLvFile(dialog)
        result = dialog.exec_() # modal type show the window
        print("result:%d"% result)
        return "abc", "cdef"

