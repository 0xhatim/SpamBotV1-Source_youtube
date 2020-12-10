try:
    import sys
    import requests
    import time
    import uuid
    from PyQt5.QtCore import pyqtSlot,QThread,pyqtSignal
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets, QtGui
    from PyQt5.QtGui import *
    from PyQt5.uic import loadUi
    import os
    import random
    from file import Ui_Dialog
    import threading
except Exception as e:
    print(e)
    input("Enter To exit")
    sys.exit()
try:

    proxies_file = open('proxy.txt',"r").read().splitlines()
except Exception as e:
    print(e)
    input("enter to exit")
    sys.exit()

try:

    proxies_file = open('combo.txt',"r").read().splitlines()
except Exception as e:
    print(e)
    input("enter to exit")
    sys.exit()



print("""
        # Free Python Bot Spam #
    * All rights To Mexaw Alotebi : IG @31421 | telegram @mexaw
    * Falcon Digital Cumminty * 

""")



class Main(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("MEXAW REPORT SPAM V1")
        self.tasb_disable()
        self.Run = False
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.attack)
        self.counter = 0 

    def tasb_disable(self):
        self.tabWidget.tabBar().setVisible(False)
    
    def login(self):
        serial = self.lineEdit.text()
        if serial == "admin":

            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.about(self, "bad login", "you are not admin ")

    def attack(self):
        if self.Run is False:

            self.counter+=1
            print("number Of threads !",self.counter)
            threading.Thread(target=real_attack).start()
            self.Run = True 

        else:
            print("already runnig")

class real_attack():
    def __init__(self):
        while True:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
