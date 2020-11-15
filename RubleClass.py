from PyQt5.QtCore import QObject, pyqtSignal

class RubleClass(QObject):
    setRuble = pyqtSignal(int)

    def __init__(self, textEdit_2):
        super().__init__()
        print("67")
        self.textEdit_2 = textEdit_2

    def update(self,value):
        print("6")
        if value > 0:
            self.textEdit_2 = self.textEdit_2 * 2
        else:
            self.textEdit_2 = self.textEdit_2 / 2

    def getRuble(self):
        print("7")
        return str(self.textEdit_2)