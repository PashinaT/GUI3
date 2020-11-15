from PyQt5.QtCore import QObject, pyqtSignal

class DollarClass(QObject):
    setDollar = pyqtSignal(int)

    def __init__(self, dollar):
        super().__init__()
        self.dollar = dollar

    def update(self,value):
        if value > 0:
            self.dollar = self.dollar * 2
        else:
            self.dollar = self.dollar / 2

    def getDollar(self):
        return str(self.dollar)