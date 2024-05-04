# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:00:24 2024

@author: 33695
"""

import sys
from map_poke1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt


class XXXXWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.sachaX = 310
        self.sachaY = 510
        self.sacha_dx = 0
        self.sacha_dy = 0
        self.sacha_up    = 0
        self.sacha_down  = 0
        self.sacha_left  = 0
        self.sacha_right = 0
        self.name = "down0"
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.sacha_dy = -4
            
            if (self.sacha_up % 6) == 4:
                self.name = "up0"
            elif (self.sacha_up % 12) == 1:
                self.name = "up1"
            elif (self.sacha_up % 12) == 7:
                self.name = "up2"
            
            self.sacha_up += 1
        
        if event.key() == Qt.Key_Down:
            self.sacha_dy = 4
            
            if (self.sacha_down % 6) == 4:
                self.name = "down0"
            elif (self.sacha_down % 12) == 1:
                self.name ="down1"
            elif (self.sacha_down % 12) == 7:
                self.name = "down2"
        
            self.sacha_down += 1
        
        if event.key() == Qt.Key_Left:
            self.sacha_dx = -4
            
            if (self.sacha_left % 6) == 4:
                self.name = "left0"
            elif (self.sacha_left % 12) == 1:
                self.name = "left1"
            elif (self.sacha_left % 12) == 7:
                self.name = "left2"
            
            self.sacha_left += 1
        
        if event.key() == Qt.Key_Right:
            self.sacha_dx = 4
            
            if (self.sacha_right % 6) == 4:
                self.name = "right0"
            elif (self.sacha_right % 12) == 1:
                self.name = "right1"
            elif (self.sacha_right % 12) == 7:
                self.name = "right2"
            
            self.sacha_right += 1
        
        if self.sacha_dx != 0 and self.sacha_dy != 0:
            self.sacha_dx = round(self.sacha_dx * 3/4)
            self.sacha_dy = round(self.sacha_dy * 3/4)
        
        
        self.update_position()
    
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.sacha_dy = 0
        
        if event.key() == Qt.Key_Down:
            self.sacha_dy = 0
        
        if event.key() == Qt.Key_Left:
            self.sacha_dx = 0
        
        if event.key() == Qt.Key_Right:
            self.sacha_dx = 0
        
        
        self.update_position()
        
    
    def check_position(self):
        if self.sachaX < 0:
            self.sachaX = 0
        if self.sachaX > 1071:
            self.sachaX = 1071
        if self.sachaY < 0:
            self.sachaY = 0
        if self.sachaY > 696:
            self.sachaY = 696
    
    def update_position(self):
        self.sachaX += self.sacha_dx
        self.sachaY += self.sacha_dy
        self.check_position()
        
        self.label_2.setPixmap(QtGui.QPixmap("animation/" + self.name + ".png"))
        self.label_2.setGeometry(QtCore.QRect(self.sachaX, self.sachaY, 19, 25))
        
        
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = XXXXWindow()
        mainWin.show()
        app.exec_()
    run_app()