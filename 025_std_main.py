from PyQt4 import QtGui

if __name__=='__main__':
    import sys
    app=QtGui.QApplication(sys.argv)
    Form=QtGui.QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
