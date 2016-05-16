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

        self.productInfo = ProductInfo()
        self.ui.lineEditCustomer.setText(_translate("MainWindow", self.productInfo.customer, None))
        self.ui.lineEditProdPN.setText(_translate("MainWindow", self.productInfo.pn, None))

        self.testInfo = TestInfo()
        self.ui.lineEditStation.setText(_translate("MainWindow", self.testInfo.station, None))
        self.ui.lineEditFixtureSN.setText(_translate("MainWindow", self.testInfo.fixtureSN, None))
        
class InitTest():
    #def __init__(self):
        
    def get_mac_address(self):
        import uuid
        mac = uuid.UUID(int =  uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e+2] for e in range(0,11,2)])
        #renurn mac

class ProductInfo():
    def __init__(self):
        import ConfigParser
        conf = ConfigParser.ConfigParser()
        conf.read("03-000015-001_FCT.ini")
        self.customer = conf.get("product", "customer")
        self.pn = conf.get("product", "pn")
        self.name = conf.get("product", "name")
        
class TestInfo():
    def __init__(self):
        import ConfigParser
        conf = ConfigParser.ConfigParser()
        conf.read("03-000015-001_FCT.ini")
        self.station = conf.get("test", "station")
        self.fixtureSN = conf.get("test", "fixtureSN")



        
if __name__ == '__main__':
    from PyQt4 import QtGui
    import sys

    app=QtGui.QApplication(sys.argv)
    window=MyMainWindow()
    window.show()
    sys.exit(app.exec_())
