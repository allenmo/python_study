from PyQt4.QtGui import QDialog, QMainWindow
from ui_linear import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def  __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.okButton.clicked.connect(self.ui.lineEdit.clear)
        
if __name__ == '__main__':
    from PyQt4 import QtGui
    import sys

    app=QtGui.QApplication(sys.argv)
    window=MyMainWindow()
    window.show()
    sys.exit(app.exec_())
