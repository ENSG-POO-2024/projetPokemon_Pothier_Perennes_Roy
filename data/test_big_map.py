# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:17:21 2024

@author: Ordi
"""


import sys
from time import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(661,541)
        # self.setGeometry(400,150,661,541)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(0,0,661,541)
        self.fond = QtWidgets.QLabel(self.centralwidget)
        self.fond.setGeometry(QtCore.QRect(-260,-530,1920,1280))
        self.fond.setText("")
        self.fond.setPixmap(QtGui.QPixmap("images/divers/big_map.png"))
        self.fond.setScaledContents(True)
        self.fond.setObjectName("fond")
        self.sacha = QtWidgets.QLabel(self.centralwidget)
        self.sacha.setGeometry(QtCore.QRect(202, 200, 19, 25))
        self.sacha.setText("")
        self.sacha.setPixmap(QtGui.QPixmap("images/animation/down0.png"))
        self.sacha.setScaledContents(True)
        self.sacha.setObjectName("sacha")
        self.inventairemarron = QtWidgets.QLabel(self.centralwidget)
        self.inventairemarron.setGeometry(QtCore.QRect(10, 10, 641, 521))
        self.inventairemarron.setText("")
        self.inventairemarron.setPixmap(QtGui.QPixmap("inventory.png"))
        self.inventairemarron.setScaledContents(True)
        self.inventairemarron.setObjectName("inventairemarron")
        self.fondcombat = QtWidgets.QLabel(self.centralwidget)
        self.fondcombat.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.fondcombat.setText("")
        self.fondcombat.setPixmap(QtGui.QPixmap("images/divers/fond combat.PNG"))
        self.fondcombat.setScaledContents(True)
        self.fondcombat.setObjectName("fondcombat")
        self.inventairemarron.hide()
        self.fondcombat.hide()
        self.speed = 4
        self.time = time()
        self.name = "down0"
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.dir = 1
        elif event.key() == Qt.Key_Down:
            self.dir = 2
        elif event.key() == Qt.Key_Left:
            self.dir = 3
        elif event.key() == Qt.Key_Right:
            self.dir = 4
        elif event.key() == Qt.Key_Return:
            self.inventairemarron.show()
            self.dir = 0
            self.moves = 0
        else:
            return
        self.update_position()
    
    def check_position(self):
        if self.dir == 1:
            pass
            if self.fond.y() > - self.speed:
                self.sacha.move(self.sacha.x(), self.sacha.y() - self.speed)
                self.fond.move(self.fond.x(), self.fond.y() - self.speed)
            elif self.fond:
                pass
            
            if self.fond.y() + self.fond.height() < self.height() + self.speed and self.dir == 2:
                self.sacha.move(self.sacha.x(), self.sacha.y() + self.speed)
                self.fond.move(self.fond.x(), self.fond.y() + self.speed)
            
            if self.fond.x() > - self.speed and self.dir == 3:
                self.sacha.move(self.sacha.x() - self.speed, self.sacha.y())
                self.fond.move(self.fond.x() - self.speed, self.fond.y())
            
            if self.fond.x() + self.fond.width() < self.width() + self.speed and self.dir == 4:
                self.sacha.move(self.sacha.x() + self.speed, self.sacha.y())
                self.fond.move(self.fond.x() + self.speed, self.fond.y())
    
    def update_position(self):
        self.check_position()
        name = {1:"up", 2:"down", 3:"left", 4:"right", 0: "down"}[self.dir]
        dx = {0:0, 1:0, 2: 0, 3:1, 4:-1}[self.dir] * self.speed
        dy = {0:0, 1:1, 2:-1, 3:0, 4: 0}[self.dir] * self.speed
        
        if time() - self.time < 0.5:
        
            if (self.moves % 6) == 4:
                self.name = name + "0"
            elif (self.moves % 12) == 1:
                self.name = name + "1"
            elif (self.moves % 12) == 7:
                self.name = name + "2"
            self.moves += 1
        
        else:
            self.moves = 0
            self.name = name + "0"
    
        self.sacha.setPixmap(QtGui.QPixmap("images/animation/" + self.name + ".png"))
        self.fond.move(self.fond.x() + dx, self.fond.y() + dy)
        self.time = time()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())