def cmtom(self):
    self.label.setText('Centimeter')
    self.label_2.setText('Meter')
    x=float(self.first.text())
    y=str(x*0.01)
    self.second.setText(y)

def cmtoinch(self):
    self.label.setText('Centimeter')
    self.label_2.setText('Inch')
    x=float(self.first.text())
    y=str(x/2.54)
    self.second.setText(y)

def mtofoot(self):
    self.label.setText('Meter')
    self.label_2.setText('Foot')
    x=float(self.first.text())
    y=str(x/0.3048)
    self.second.setText(y)