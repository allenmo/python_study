from ui_linear import Ui_MainWindow

class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)


if __name__ == '__main__':
    from PyQt4 import QtGui
    import sys

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
