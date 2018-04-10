def cmtom(self):
    self.invert.clicked.connect(lambda: mtocm(self))
    self.label.setText('Centimeter')
    self.label_2.setText('Meter')
    x=float(self.first.text())
    y=str(x*0.01)
    self.second.setText(y)
    

def mtocm(self):
    self.label.setText('Meter')
    self.label_2.setText('Centimeter')
    x=float(self.first.text())
    y=str(x*100)
    self.second.setText(y)

def cmtoinch(self):
    self.invert.clicked.connect(lambda: inchtocm(self))
    self.label.setText('Centimeter')
    self.label_2.setText('Inch')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format(x/2.54)))
    self.second.setText(y)

def inchtocm(self):
    self.label.setText('Inch')
    self.label_2.setText('Centimeter')
    x=float(self.first.text())
    y=str(x*2.54)
    self.second.setText(y)

def mtofoot(self):
    self.invert.clicked.connect(lambda: foottom(self))
    self.label.setText('Meter')
    self.label_2.setText('Foot')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format(x/0.3048)))
    self.second.setText(y)

def foottom(self):
    self.label.setText('Foot')
    self.label_2.setText('Meter')
    x=float(self.first.text())
    y=str(x*0.3048)
    self.second.setText(y)

def mtoyard(self):
    self.invert.clicked.connect(lambda: yardtom(self))
    self.label.setText('Meter')
    self.label_2.setText('Yard')
    x=float(self.first.text())
    y=str(x*1.09361)
    self.second.setText(y)

def yardtom(self):
    self.label.setText('Yard')
    self.label_2.setText('Meter')
    x=float(self.first.text())
    y=str(x/1.09361)
    self.second.setText(y)

def kgtog(self):
    self.invert.clicked.connect(lambda: gtokg(self))
    self.label.setText('Kilogram')
    self.label_2.setText('Gram')
    x=float(self.first.text())
    y=str(x*1000)
    self.second.setText(y)

def gtokg(self):
    self.label_2.setText('Kilogram')
    self.label.setText('Gram')
    x=float(self.first.text())
    y=str(x/1000.0)
    self.second.setText(y)

def kgtopound(self):
    self.invert.clicked.connect(lambda: poundtokg(self))
    self.label.setText('Kilogram')
    self.label_2.setText('Pound')
    x=float(self.first.text())
    y=str(x*2.20462)
    self.second.setText(y)

def poundtokg(self):
    self.label_2.setText('Kilogram')
    self.label.setText('Pound')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format(x/2.20462)))
    self.second.setText(y)

def kgtoounce(self):
    self.invert.clicked.connect(lambda: ouncetokg(self))
    self.label.setText('Kilogram')
    self.label_2.setText('Ounce')
    x=float(self.first.text())
    y=str(x*35.274)
    self.second.setText(y)

def ouncetokg(self):
    self.label.setText('Ounce')
    self.label_2.setText('Kilogram')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format(x/35.274)))
    self.second.setText(y)

def kgtotonne(self):
    self.invert.clicked.connect(lambda: tonnetokg(self))
    self.label.setText('Kilogram')
    self.label_2.setText('Tonne')
    x=float(self.first.text())
    y=str(x*0.0001)
    self.second.setText(y)

def tonnetokg(self):
    self.label.setText('Tonne')
    self.label_2.setText('Kilogram')
    x=float(self.first.text())
    y=str(x*1000.0)
    self.second.setText(y)

def celtofah(self):
    self.invert.clicked.connect(lambda: fahtocel(self))
    self.label.setText('Celcius')
    self.label_2.setText('Fahrenheit')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format(x*1.8))+32)
    self.second.setText(y)

def fahtocel(self):
    self.label.setText('Fahrenheit')
    self.label_2.setText('Celcius')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format((x-32)/1.8)))
    self.second.setText(y)

def celtokel(self):
    self.invert.clicked.connect(lambda: keltocel(self))
    self.label.setText('Celcius')
    self.label_2.setText('Kelvin')
    x=float(self.first.text())
    y=str(x+273.15)
    self.second.setText(y)

def keltocel(self):
    self.label.setText('Kelvin')
    self.label_2.setText('Celcius')
    x=float(self.first.text())
    y=str(x-273.15)
    self.second.setText(y)

def fahtokel(self):
    self.invert.clicked.connect(lambda: keltofah(self))
    self.label.setText('Fahrenheit')
    self.label_2.setText('Kelvin')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format((x+459.67)*(5/9))))
    self.second.setText(y)

def keltofah(self):
    self.label.setText('Kelvin')
    self.label_2.setText('Fahrenheit')
    x=float(self.first.text())
    y=str(float("{0:.5f}".format((x*1.8)-459.67)))
    self.second.setText(y)
