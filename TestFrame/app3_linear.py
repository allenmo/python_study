from PyQt4.QtGui import QMainWindow
from ui_linear import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)

        self.okButton.clicked.connect(self.lineEdit.clear)

if __name__ == '__main__':
    from PyQt4 import QtGui
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()

    sys.exit(app.exec_())
