import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from func import *



class converter(QDialog):
    def __init__(self):
        super(converter,self).__init__()
        loadUi('main.ui',self)
        self.setWindowTitle('Unit Converter')
        self.cmtom.clicked.connect(lambda: cmtom(self))
        self.cmtoinch.clicked.connect(lambda: cmtoinch(self))
        self.mtofoot.clicked.connect(lambda: mtofoot(self))
        

app=QApplication(sys.argv)
widget=converter()
widget.show()
sys.exit(app.exec_())