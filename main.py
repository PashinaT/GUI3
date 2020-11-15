from PyQt5 import uic
from PyQt5.QtWidgets import *
from DollarClass import DollarClass
from RubleClass import RubleClass
from PetrolClass import PetrolClass
import sys

top = 400
left = 400
width = 500
height = 500

def buttonClicked():
    petrolNew = float(window.textEdit_3.toPlainText())
    currentPetrol = float(petrol.getPetrol())
    if petrolNew>currentPetrol:
        ruble.setRuble.emit(1)
        window.textEdit_2.setText(ruble.getRuble())
    if petrolNew<currentPetrol:
        dollar.setDollar.emit(1)
        window.textEdit.setText(dollar.getDollar())
    petrol.setPetrol(petrolNew)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = uic.loadUi("qtDesign.ui")
    window.textEdit.setText("2")
    window.textEdit_2.setText("40")
    window.textEdit_3.setText("80")
    petrol=PetrolClass(80)
    dollar = DollarClass(2)
    dollar.setDollar.connect(dollar.update)
    ruble = RubleClass(40)
    ruble.setRuble.connect(ruble.update)
    window.pushButton.clicked.connect(buttonClicked)
    window.show()
    app.exec()