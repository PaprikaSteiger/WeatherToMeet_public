# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from back import weather



qss = '''

QPushButton{
    background-color: rgb(255, 255, 255);
	font: 12pt "MV Boli";
	color: rgb(0, 32, 96);
	border-radius: 10px;

}
QPushButton:hover{
    background-color: rgb(218, 227, 243)
}
'''


qss1 = '''

QPushButton{
    background-color: rgb(255, 255, 255);
	font: 12pt "MV Boli";
	color:  rgb(168, 168, 168);
	border-radius: 10px;
}
'''




class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(540, 680)
        Weather.setStyleSheet("background-color: rgb(0, 32, 96);\n"
"")


        #calla the back function
        fecha, location, categorie, activities, temperature = weather()
        self.size = len(activities)
        

        self.centralwidget = QtWidgets.QWidget(Weather)
        self.centralwidget.setObjectName("centralwidget")
        self.fondo1 = QtWidgets.QFrame(self.centralwidget)
        self.fondo1.setGeometry(QtCore.QRect(30, 20, 480, 640))
        self.fondo1.setStyleSheet("background-color: rgb(218, 227, 243);\n"
"border-radius: 20px;" )
        self.fondo1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo1.setObjectName("fondo1")
        self.icon = QtWidgets.QLabel(self.fondo1)
        self.icon.setGeometry(QtCore.QRect(60, 110, 141, 121))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap('static/' + categorie + ".png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.frameFecha = QtWidgets.QFrame(self.fondo1)
        self.frameFecha.setGeometry(QtCore.QRect(260, 120, 171, 161))
        self.frameFecha.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"border-radius: 20px;\n"
"")
        self.frameFecha.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFecha.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFecha.setObjectName("frameFecha")
        self.Fecha = QtWidgets.QLabel(self.frameFecha)
        self.Fecha.setGeometry(QtCore.QRect(10, 20, 150, 111))
        self.Fecha.setAcceptDrops(True)
        self.Fecha.setStyleSheet("font: 18pt \"MV Boli\";\n"
"color: rgb(0, 32, 96);")
        self.Fecha.setTextFormat(QtCore.Qt.AutoText)
        self.Fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.Fecha.setWordWrap(True)
        self.Fecha.setObjectName("Fecha")
        self.fondo2 = QtWidgets.QFrame(self.fondo1)
        self.fondo2.setGeometry(QtCore.QRect(20, 360, 441, 261))
        self.fondo2.setStyleSheet("background-color: rgb(255, 217, 102);\n"
"border-radius: 20px;")
        self.fondo2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo2.setObjectName("fondo2")
        self.actividad = QtWidgets.QLabel(self.fondo2)
        self.actividad.setGeometry(QtCore.QRect(20, 20, 391, 171))
        self.actividad.setStyleSheet("font: 18pt \"MV Boli\";\n"
"color: rgb(0, 32, 96);")
        self.actividad.setAlignment(QtCore.Qt.AlignCenter)
        self.actividad.setWordWrap(True)
        self.actividad.setObjectName("actividad")
        self.Previous = QtWidgets.QPushButton(self.fondo2)
        self.Previous.setGeometry(QtCore.QRect(20, 210, 81, 31))

        self.Previous.setStyleSheet(qss)

        """
        self.Previous.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MV Boli\";\n"
"color: rgb(0, 32, 96);\n"
"border-radius: 10px;\n"
"" )"""
       

        self.Previous.setObjectName("Previous")
        self.Next = QtWidgets.QPushButton(self.fondo2)
        self.Next.setGeometry(QtCore.QRect(340, 210, 81, 31))
        self.Next.setStyleSheet(qss)		
        
        self.Next.setObjectName("Next")
        self.Temp = QtWidgets.QLabel(self.fondo1)
        self.Temp.setGeometry(QtCore.QRect(100, 260, 81, 51))
        self.Temp.setStyleSheet("font: 18pt \"MV Boli\";\n"
"color: rgb(0, 32, 96);")
        self.Temp.setObjectName("Temp")
        self.City = QtWidgets.QLabel(self.fondo1)
        self.City.setGeometry(QtCore.QRect(60, 220, 181, 51))
        self.City.setStyleSheet("font: 18pt \"MV Boli\";\n"
"color: rgb(0, 32, 96);")
        self.City.setObjectName("City")
        self.Titulo = QtWidgets.QLabel(self.fondo1)
        self.Titulo.setGeometry(QtCore.QRect(100, 10, 301, 51))
        self.Titulo.setStyleSheet("font: 25pt \"MV Boli\";\n"
"color: rgb(0, 32, 96);")
        self.Titulo.setObjectName("Titulo")
        Weather.setCentralWidget(self.centralwidget)

        self.retranslateUi(Weather, fecha, temperature, location, activities)
        QtCore.QMetaObject.connectSlotsByName(Weather)
        self.counter = 0
        self.Previous.setEnabled(False)
        self.Previous.setStyleSheet(qss1)




        self.activites = activities


        self.Next.clicked.connect(self.clickNext)
        self.Previous.clicked.connect(self.clickPrevious)



        #Only 1 activite diav¿bles navegation items

        if self.size == 1:
        	self.Next.setEnabled(False)
        	self.Next.setStyleSheet(qss1)
        	self.Previous.setEnabled(False)
        	self.Previous.setStyleSheet(qss1)


    def retranslateUi(self, Weather, fecha, temperature, location, activities):
        _translate = QtCore.QCoreApplication.translate
        Weather.setWindowTitle(_translate("Weather", "Weather ToMeet"))
        self.Fecha.setText(_translate("Weather", fecha))
        self.actividad.setText(_translate("Weather", activities[0]))
        self.Previous.setText(_translate("Weather", "Previous"))
        self.Next.setText(_translate("Weather", "Next"))
        self.Temp.setText(_translate("Weather", temperature))
        self.City.setText(_translate("Weather", location))
        self.Titulo.setText(_translate("Weather", "Weather ToMeet?"))

       
        


    def clickNext(self):
    	self.Previous.setEnabled(True)
    	self.Previous.setStyleSheet(qss)
    	self.counter += 1
    	self.actividad.setText(self.activites[self.counter])
    	if self.counter == self.size - 1:
    		self.Next.setEnabled(False)
    		self.Next.setStyleSheet(qss1)

    def clickPrevious(self):
    	self.Next.setEnabled(True)
    	self.Next.setStyleSheet(qss)
    	self.counter -= 1
    	self.actividad.setText(self.activites[self.counter])
    	if self.counter == 0:
    		self.Previous.setEnabled(False)
    		self.Previous.setStyleSheet(qss1)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Weather = QtWidgets.QMainWindow()
    ui = Ui_Weather()
    ui.setupUi(Weather)
    Weather.show()
    sys.exit(app.exec_())
