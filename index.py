import sys
from PyQt5.QtCore import pyqtSlot,Qt
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
        self.mtoyard.clicked.connect(lambda: mtoyard(self))
        self.kgtog.clicked.connect(lambda: kgtog(self))
        self.kgtopound.clicked.connect(lambda: kgtopound(self))
        self.kgtoounce.clicked.connect(lambda: kgtoounce(self))
        self.kgtotonne.clicked.connect(lambda: kgtotonne(self))
        self.celtofah.clicked.connect(lambda: celtofah(self))
        self.celtokel.clicked.connect(lambda: celtokel(self))
        self.fahtokel.clicked.connect(lambda: fahtokel(self))

app=QApplication(sys.argv)
widget=converter()
# p = widget.palette()
# p.setColor(widget.backgroundRole(), Qt.blue)
# widget.setPalette(p)
widget.show()
sys.exit(app.exec_())