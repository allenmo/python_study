from PyQt4 import QtGui
from 001_dialog import *

if __name__=='__main__':
    import sys
    app=QtGui.QApplication(sys.argv)
    Form=QtGui.QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
