from PyQt4.QtGui import QMainWindow
from ui_linear import Ui_MainWindow
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


class MyMainWindow(QMainWindow):
    def  __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.initTest = InitTest()
        self.ui.lineEditComputerID.setText(_translate("MainWindow", self.initTest.get_mac_address(), None))
        
class InitTest():
    #def __init__(self):
        
    def get_mac_address(self):
        import uuid
        mac = uuid.UUID(int =  uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e+2] for e in range(0,11,2)])
        #renurn mac

        
if __name__ == '__main__':
    from PyQt4 import QtGui
    import sys

    app=QtGui.QApplication(sys.argv)
    window=MyMainWindow()
    window.show()
    sys.exit(app.exec_())
